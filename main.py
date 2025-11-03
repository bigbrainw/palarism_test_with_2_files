from sentence_transformers import SentenceTransformer, util
import re, numpy as np

def split_sentences_zh(text):
    # 粗略中文斷句：句號/問號/驚嘆號/換行
    parts = re.split(r'(?<=[。！？])\s*|\n+', text.strip())
    return [p for p in parts if p]

def detect_sequential_matches(matches, threshold=3):
    """Detect if sentences appear in the same sequential order in both articles"""
    if len(matches) < threshold:
        return []
    
    # Sort by position in article A
    sorted_matches = sorted(matches, key=lambda x: x[3])  # x[3] is index in A
    
    sequences = []
    current_seq = [sorted_matches[0]]
    
    for i in range(1, len(sorted_matches)):
        prev_a_idx, prev_b_idx = sorted_matches[i-1][3], sorted_matches[i-1][4]
        curr_a_idx, curr_b_idx = sorted_matches[i][3], sorted_matches[i][4]
        
        # Check if both indices are sequential (allow small gaps)
        if (curr_a_idx - prev_a_idx <= 3 and curr_b_idx - prev_b_idx <= 3 and 
            curr_b_idx > prev_b_idx):
            current_seq.append(sorted_matches[i])
        else:
            if len(current_seq) >= threshold:
                sequences.append(current_seq)
            current_seq = [sorted_matches[i]]
    
    if len(current_seq) >= threshold:
        sequences.append(current_seq)
    
    return sequences

print("=" * 80)
print("PLAGIARISM DETECTION REPORT")
print("=" * 80)

# Load model
print("\n[1/5] Loading multilingual sentence transformer model...")
m = SentenceTransformer("sentence-transformers/paraphrase-multilingual-mpnet-base-v2")

# Load articles
print("[2/5] Loading articles...")
with open("article_A.txt", "r", encoding="utf-8") as f:
    text_A = f.read()
    A = split_sentences_zh(text_A)

with open("article_B.txt", "r", encoding="utf-8") as f:
    text_B = f.read()
    B = split_sentences_zh(text_B)

print(f"  Article A (Original): {len(A)} sentences")
print(f"  Article B (Suspected): {len(B)} sentences")

# Encode sentences
print("[3/5] Encoding sentences...")
embA = m.encode(A, convert_to_tensor=True, normalize_embeddings=True)
embB = m.encode(B, convert_to_tensor=True, normalize_embeddings=True)

# Document-level similarity
print("[4/5] Calculating document-level similarity...")
full_embA = m.encode([text_A], convert_to_tensor=True, normalize_embeddings=True)
full_embB = m.encode([text_B], convert_to_tensor=True, normalize_embeddings=True)
doc_similarity = util.cos_sim(full_embA, full_embB).item()

# Sentence-level similarity matrix (|A| x |B|)
print("[5/5] Analyzing sentence-level matches...")
sim = util.cos_sim(embA, embB).cpu().numpy()

# Find matches for each sentence in A
THRESHOLD = 0.70  # Lowered to catch more subtle paraphrasing
matches = []
matched_a_indices = set()

for i, row in enumerate(sim):
    j = int(np.argmax(row))
    score = row[j]
    if score >= THRESHOLD:
        matches.append((score, A[i], B[j], i, j))  # Include indices
        matched_a_indices.add(i)

# Calculate statistics
plagiarism_percentage = (len(matched_a_indices) / len(A)) * 100 if A else 0
matches.sort(reverse=True, key=lambda x: x[0])

# Detect sequential matches
sequential_blocks = detect_sequential_matches(matches, threshold=3)

# Print results
print("\n" + "=" * 80)
print("SUMMARY STATISTICS")
print("=" * 80)
print(f"Document-level similarity: {doc_similarity:.2%}")
print(f"Sentences matched: {len(matched_a_indices)} / {len(A)} ({plagiarism_percentage:.1f}%)")
print(f"Average match score: {np.mean([m[0] for m in matches]):.3f}" if matches else "N/A")
print(f"Sequential blocks found: {len(sequential_blocks)}")

# Plagiarism verdict
print("\n" + "=" * 80)
print("VERDICT")
print("=" * 80)
if plagiarism_percentage >= 50:
    print("⚠️  HIGH RISK: Significant plagiarism detected!")
elif plagiarism_percentage >= 25:
    print("⚠️  MODERATE RISK: Substantial similarity found")
elif plagiarism_percentage >= 10:
    print("⚠️  LOW RISK: Some matching content detected")
else:
    print("✓  MINIMAL RISK: Little to no plagiarism detected")

# Print sequential blocks
if sequential_blocks:
    print("\n" + "=" * 80)
    print(f"SEQUENTIAL BLOCKS (Sentences in same order - STRONG PLAGIARISM INDICATOR)")
    print("=" * 80)
    for idx, seq in enumerate(sequential_blocks[:5], 1):  # Show top 5 blocks
        print(f"\n--- Sequential Block #{idx} ({len(seq)} consecutive sentences) ---")
        avg_score = np.mean([s[0] for s in seq])
        print(f"Average similarity: {avg_score:.3f}")
        for score, a, b, i, j in seq[:3]:  # Show first 3 sentences of each block
            print(f"\n[A-{i+1}] {a}")
            print(f"[B-{j+1}] {b}")
            print(f"Score: {score:.3f}")
        if len(seq) > 3:
            print(f"\n... and {len(seq)-3} more sentences in this block")

# Print top individual matches
print("\n" + "=" * 80)
print(f"TOP 20 INDIVIDUAL MATCHES (Threshold: {THRESHOLD})")
print("=" * 80)
for idx, (score, a, b, i, j) in enumerate(matches[:20], 1):
    severity = "🔴 VERY HIGH" if score >= 0.90 else "🟠 HIGH" if score >= 0.80 else "🟡 MODERATE"
    print(f"\n#{idx} - Similarity: {score:.3f} {severity}")
    print(f"[A-{i+1}] {a}")
    print(f"[B-{j+1}] {b}")
    print("-" * 80)

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
