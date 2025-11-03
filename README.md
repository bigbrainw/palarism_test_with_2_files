# Plagiarism Detection System

A sophisticated semantic plagiarism detection tool that uses AI-powered sentence transformers to identify copied or paraphrased content between two articles. Supports multilingual text including Chinese, English, and other languages.

## Features

✨ **Advanced Detection Capabilities:**
- 🔍 **Sentence-level similarity analysis** - Identifies matching sentences with paraphrasing
- 📊 **Document-level comparison** - Calculates overall article similarity
- 🔗 **Sequential block detection** - Finds consecutive sentences in the same order (strong plagiarism indicator)
- 📈 **Statistical analysis** - Provides plagiarism percentage and risk assessment
- 🌍 **Multilingual support** - Works with Chinese, English, and 50+ other languages
- 🎯 **Smart thresholding** - Catches subtle paraphrasing while avoiding false positives

## Requirements

- Python 3.7 or higher
- Required libraries:
  - `sentence-transformers` - AI model for semantic similarity
  - `numpy` - Numerical computations
  - `re` (built-in) - Text processing

## Installation

1. **Clone or download this repository**

2. **Install dependencies:**
```bash
pip install -r requriements.txt
```

Or using a virtual environment (recommended):
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install sentence-transformers numpy
```

3. **Prepare your articles:**
   - Create `article_A.txt` - The original article
   - Create `article_B.txt` - The suspected plagiarized article
   - Both files should be in UTF-8 encoding

## Usage

### Basic Usage

1. Place your two articles in the same directory as `main.py`:
   - `article_A.txt` - Original article
   - `article_B.txt` - Article to check for plagiarism

2. Run the script:
```bash
python main.py
```

3. The program will generate a comprehensive plagiarism report showing:
   - Overall plagiarism percentage
   - Document-level similarity score
   - Risk assessment (HIGH/MODERATE/LOW/MINIMAL)
   - Sequential blocks of copied content
   - Top 20 individual sentence matches with scores

### Sample Output

```
================================================================================
PLAGIARISM DETECTION REPORT
================================================================================

[1/5] Loading multilingual sentence transformer model...
[2/5] Loading articles...
  Article A (Original): 45 sentences
  Article B (Suspected): 42 sentences
[3/5] Encoding sentences...
[4/5] Calculating document-level similarity...
[5/5] Analyzing sentence-level matches...

================================================================================
SUMMARY STATISTICS
================================================================================
Document-level similarity: 78.50%
Sentences matched: 35 / 45 (77.8%)
Average match score: 0.845
Sequential blocks found: 3

================================================================================
VERDICT
================================================================================
⚠️  HIGH RISK: Significant plagiarism detected!

================================================================================
SEQUENTIAL BLOCKS (Sentences in same order - STRONG PLAGIARISM INDICATOR)
================================================================================

--- Sequential Block #1 (5 consecutive sentences) ---
Average similarity: 0.892
...
```

## How It Works

### 1. **Sentence Splitting**
The system intelligently splits articles into sentences using punctuation markers (。！？for Chinese, with support for other languages).

### 2. **Semantic Encoding**
Uses the `paraphrase-multilingual-mpnet-base-v2` model to convert each sentence into a 768-dimensional vector that captures its meaning, not just exact words.

### 3. **Similarity Calculation**
- Computes cosine similarity between all sentence pairs
- Identifies best matches for each sentence in Article A
- Filters results using a threshold (default: 0.70)

### 4. **Pattern Detection**
- **Sequential blocks**: Detects 3+ consecutive sentences that appear in the same order
- **Document similarity**: Compares entire articles for overall similarity
- **Statistical analysis**: Calculates plagiarism percentage and risk levels

### 5. **Risk Assessment**
- **HIGH RISK** (≥50%): Significant plagiarism detected
- **MODERATE RISK** (25-49%): Substantial similarity found
- **LOW RISK** (10-24%): Some matching content detected
- **MINIMAL RISK** (<10%): Little to no plagiarism detected

## Configuration

You can adjust the detection sensitivity by modifying these parameters in `main.py`:

```python
THRESHOLD = 0.70  # Line 75 - Minimum similarity score (0.0-1.0)
                  # Lower = more sensitive, Higher = more strict
                  # Recommended range: 0.65-0.80

# Sequential block detection
detect_sequential_matches(matches, threshold=3)  # Line 91
# threshold: Minimum consecutive sentences to flag as a block
```

### Similarity Score Guide:
- **0.90-1.00**: Nearly identical or direct copy
- **0.80-0.89**: Very high similarity, likely paraphrasing
- **0.70-0.79**: Moderate similarity, possible paraphrasing
- **0.60-0.69**: Low similarity, may be coincidental
- **Below 0.60**: Different content

## What It Can Detect

✅ **Detectable:**
- Direct copying (exact matches)
- Close paraphrasing with synonym substitution
- Sentence restructuring with same meaning
- Translation-based plagiarism
- Reordered sentences (detected individually)
- Mixed plagiarism (partial copying)

❌ **Limitations:**
- Heavily restructured ideas with completely different wording
- Concept plagiarism without language similarity
- Extreme summarization or expansion
- Plagiarism from sources not provided

## File Structure

```
palarism/
├── main.py              # Main plagiarism detection script
├── article_A.txt        # Original article (to be created)
├── article_B.txt        # Suspected article (to be created)
├── README.md            # This file
└── venv/                # Virtual environment (optional)
```

## Technical Details

**Model Information:**
- **Model**: `sentence-transformers/paraphrase-multilingual-mpnet-base-v2`
- **Architecture**: Microsoft MPNet (Masked and Permuted Pre-training)
- **Embedding Size**: 768 dimensions
- **Languages**: 50+ languages including Chinese, English, Spanish, French, German, etc.
- **Training**: Trained on paraphrase detection tasks

**Performance:**
- First run: ~30 seconds (downloads model, ~420MB)
- Subsequent runs: ~5-10 seconds for typical articles
- Memory usage: ~2GB RAM

## Troubleshooting

### Model Download Issues
If the model fails to download:
```bash
# Set a custom cache directory
export TRANSFORMERS_CACHE=/path/to/cache
python main.py
```

### Encoding Errors
If you get encoding errors, ensure your text files are UTF-8:
```python
# Save files as UTF-8 in your text editor
# Or convert existing files:
with open('article.txt', 'r', encoding='gbk') as f:
    content = f.read()
with open('article.txt', 'w', encoding='utf-8') as f:
    f.write(content)
```

### Out of Memory
For very large articles (>1000 sentences):
- Process in chunks
- Use a machine with more RAM
- Or reduce batch size in encoding

## Future Enhancements

Potential improvements for future versions:
- [ ] Web interface for easy file uploads
- [ ] PDF and Word document support
- [ ] Batch processing multiple articles
- [ ] HTML report generation
- [ ] Citation detection (legitimate quotes vs plagiarism)
- [ ] Paragraph-level analysis
- [ ] Export results to JSON/CSV
- [ ] Multiple source comparison

## License

This project is open source and available for educational and research purposes.

## Credits

Built with:
- [Sentence Transformers](https://www.sbert.net/) by UKPLab
- [HuggingFace Transformers](https://huggingface.co/)
- [NumPy](https://numpy.org/)

## Contributing

Feel free to fork, modify, and improve this plagiarism detection system. Suggestions and pull requests are welcome!

---

**Note**: This tool is designed to assist in plagiarism detection but should not be the sole method for determining plagiarism. Human review and judgment are essential for final decisions.

