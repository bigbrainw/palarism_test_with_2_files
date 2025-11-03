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

###Output

```
================================================================================
PLAGIARISM DETECTION REPORT
================================================================================

[1/5] Loading multilingual sentence transformer model...
[2/5] Loading articles...
  Article A (Original): 31 sentences
  Article B (Suspected): 46 sentences
[3/5] Encoding sentences...
[4/5] Calculating document-level similarity...
[5/5] Analyzing sentence-level matches...

================================================================================
SUMMARY STATISTICS
================================================================================
Document-level similarity: 67.08%
Sentences matched: 19 / 31 (61.3%)
Average match score: 0.783
Sequential blocks found: 1

================================================================================
VERDICT
================================================================================
⚠️  HIGH RISK: Significant plagiarism detected!

================================================================================
SEQUENTIAL BLOCKS (Sentences in same order - STRONG PLAGIARISM INDICATOR)
================================================================================

--- Sequential Block #1 (4 consecutive sentences) ---
Average similarity: 0.826

[A-6] 當時這些教育場域具備一定程度的公共性----這群人之所以辦學校、之所以持續經營、實踐和辯證各種教育行動，是因為二十多年來他們始終相信這樣教育行動本身，能夠影響參與其中的教育工作者、學習者和家庭，長遠下來，便有機會為群體社會創造出深化學習、平等、共好 等社會影響。
[B-9] 在那個階段，實驗教育之所以存在，是因為它具有公共性——它不只是為了滿足個人的選擇，而是希望能透過教育行動，影響教師、學習者與家庭，進而讓整個社會變得更平等、更有共好意識。
Score: 0.804

[A-7] 以至於設計學校組織、課程架構、校園實質生活內涵時，我們不傾向從競爭力的角度思考教育和個體的關係，而是始終維持辯證主流價值的聲稱。
[B-10] 因此，我們設計學校的組織與課程時，並不以「競爭力」為主軸，而是持續與主流價值辯證，從理想與現實之間，找到合理的教育行動。
Score: 0.924

[A-9] 比如說，「雙語」和「國際化」是教育現場沸沸揚揚的主流價值，我們對於主流價值沒有偏見或成見，但是我們會堅持先去問：我們遇到的孩子背景是什麼？
[B-11] 例如，當「雙語」與「國際化」及許多堆疊的「教育產業名詞」成為當代學校競逐的顯學，我們並不急於追隨，而是先問：我們面對的孩子是誰？
Score: 0.829

... and 1 more sentences in this block

================================================================================
TOP 20 INDIVIDUAL MATCHES (Threshold: 0.7)
================================================================================

#1 - Similarity: 0.924 🔴 VERY HIGH
[A-7] 以至於設計學校組織、課程架構、校園實質生活內涵時，我們不傾向從競爭力的角度思考教育和個體的關係，而是始終維持辯證主流價值的聲稱。
[B-10] 因此，我們設計學校的組織與課程時，並不以「競爭力」為主軸，而是持續與主流價值辯證，從理想與現實之間，找到合理的教育行動。
--------------------------------------------------------------------------------

#2 - Similarity: 0.832 🟠 HIGH
[A-18] 這也就是為什麼我覺得，理想中的實驗學校，要帶著公共性在辦學，因爲不斷強化主流價值，並不會讓社會更平等、更豐富、更健康。
[B-17] 理想中的實驗學校，應該帶著公共性去辦學，因為唯有這樣，教育才能保持洞察力、同理心與公民性，讓孩子在結構困境中仍能創造出新的可能。
--------------------------------------------------------------------------------

#3 - Similarity: 0.829 🟠 HIGH
[A-9] 比如說，「雙語」和「國際化」是教育現場沸沸揚揚的主流價值，我們對於主流價值沒有偏見或成見，但是我們會堅持先去問：我們遇到的孩子背景是什麼？
[B-11] 例如，當「雙語」與「國際化」及許多堆疊的「教育產業名詞」成為當代學校競逐的顯學，我們並不急於追隨，而是先問：我們面對的孩子是誰？
--------------------------------------------------------------------------------

#4 - Similarity: 0.820 🟠 HIGH
[A-22] 如今，教育的選項確實看起來很豐富，但是背後的價值呢？
[B-36] 如今，少子化浪潮逼近，教育的樣貌看似豐富，但背後的價值是否也同樣多元？
--------------------------------------------------------------------------------

#5 - Similarity: 0.809 🟠 HIGH
[A-12] 還是增加文化識讀與理解？
[B-13] 語言學習的目的，是提升競爭力，還是開啟文化的理解？
--------------------------------------------------------------------------------

#6 - Similarity: 0.804 🟠 HIGH
[A-6] 當時這些教育場域具備一定程度的公共性----這群人之所以辦學校、之所以持續經營、實踐和辯證各種教育行動，是因為二十多年來他們始終相信這樣教育行動本身，能夠影響參與其中的教育工作者、學習者和家庭，長遠下來，便有機會為群體社會創造出深化學習、平等、共好 等社會影響。
[B-9] 在那個階段，實驗教育之所以存在，是因為它具有公共性——它不只是為了滿足個人的選擇，而是希望能透過教育行動，影響教師、學習者與家庭，進而讓整個社會變得更平等、更有共好意識。
--------------------------------------------------------------------------------

#7 - Similarity: 0.804 🟠 HIGH
[A-14] 當我們期望孩子認識母語、能上手外國語、同時又學習其他學科，我們怎麼感知孩子一天所擁有的注意力和好奇心？
[B-14] 我們能不能讓孩子在學會外語的同時，也理解母語、理解土地？
--------------------------------------------------------------------------------

#8 - Similarity: 0.799 🟡 MODERATE
[A-29] 因為所有的教育現場都是實驗，每一個參與教育場域的成人，都應該要尊敬這場實驗，保持謙虛、持續學習、持續記得教育是互相影響的歷程，目的在支持生命成為有意義感的個體，而不僅是塑造和灌輸最有用的知識技能。
[B-9] 在那個階段，實驗教育之所以存在，是因為它具有公共性——它不只是為了滿足個人的選擇，而是希望能透過教育行動，影響教師、學習者與家庭，進而讓整個社會變得更平等、更有共好意識。
--------------------------------------------------------------------------------

#9 - Similarity: 0.795 🟡 MODERATE
[A-17] 而不是理所當然的認為所謂的雙語環境或是國際化，就可以為台灣孩子帶來競爭力；也不會理所當然的覺得擁有了這種競爭力，個體就擁有比較幸福的未來；更不會理所當然的認為，許多有競爭力的個體，就會創造比較公平、正義同時適宜人居的社會。
[B-16] 我們不預設「雙語」或「國際化」或其他「教育產業堆疊的名詞」一定能讓孩子更幸福，也不相信競爭力必然會帶來公平社會。
--------------------------------------------------------------------------------

#10 - Similarity: 0.788 🟡 MODERATE
[A-24] 教育的聲稱看起來很多元，但是真正實踐的現場，是因為看到個體的獨特性所以長出的多元？
[B-36] 如今，少子化浪潮逼近，教育的樣貌看似豐富，但背後的價值是否也同樣多元？
--------------------------------------------------------------------------------

#11 - Similarity: 0.773 🟡 MODERATE
[A-20] 實驗學校應該是涵養這些可能性的場域。
[B-17] 理想中的實驗學校，應該帶著公共性去辦學，因為唯有這樣，教育才能保持洞察力、同理心與公民性，讓孩子在結構困境中仍能創造出新的可能。
--------------------------------------------------------------------------------

#12 - Similarity: 0.767 🟡 MODERATE
[A-27] 實驗學校被熱熱鬧鬧劃為一個獨特的類別，但其實我覺得真相是----所有的教育都是一場實驗，沒有人可以保證哪一種教育放在所有的參與個體身上，可以產出絕對預期的結果來。
[B-9] 在那個階段，實驗教育之所以存在，是因為它具有公共性——它不只是為了滿足個人的選擇，而是希望能透過教育行動，影響教師、學習者與家庭，進而讓整個社會變得更平等、更有共好意識。
--------------------------------------------------------------------------------

#13 - Similarity: 0.762 🟡 MODERATE
[A-1] 認真探究實驗教育現場的妳問我：
[B-2] 今年暑假，在台東的教師移地訓練現場，有夥伴問我：「小實光走過十年，怎麼看待現在的實驗教育趨勢與發展？
--------------------------------------------------------------------------------

#14 - Similarity: 0.748 🟡 MODERATE
[A-16] 早年，實驗教育的本質，是堅持問這些問題，持續辯證之後，有所取捨之後，再行動。
[B-9] 在那個階段，實驗教育之所以存在，是因為它具有公共性——它不只是為了滿足個人的選擇，而是希望能透過教育行動，影響教師、學習者與家庭，進而讓整個社會變得更平等、更有共好意識。
--------------------------------------------------------------------------------

#15 - Similarity: 0.748 🟡 MODERATE
[A-11] 雙語核心的意義是增加語文能力？
[B-13] 語言學習的目的，是提升競爭力，還是開啟文化的理解？
--------------------------------------------------------------------------------

#16 - Similarity: 0.726 🟡 MODERATE
[A-2] 種籽這個老牌實驗學校，怎麼看待現在實驗教育的趨勢和發展？
[B-2] 今年暑假，在台東的教師移地訓練現場，有夥伴問我：「小實光走過十年，怎麼看待現在的實驗教育趨勢與發展？
--------------------------------------------------------------------------------

#17 - Similarity: 0.721 🟡 MODERATE
[A-5] 不過，我比較有感覺得是，確實有一群學校，是在台灣教育幾乎沒有其他選項的時候，捲起袖子跟當局對話，一步一腳印把實驗學校這個人煙稀少的路徑踏成現在的道路。
[B-17] 理想中的實驗學校，應該帶著公共性去辦學，因為唯有這樣，教育才能保持洞察力、同理心與公民性，讓孩子在結構困境中仍能創造出新的可能。
--------------------------------------------------------------------------------

#18 - Similarity: 0.717 🟡 MODERATE
[A-28] 而我好希望教育當局、參與實驗教育的工作者、家長們都安靜地體認到這一點。
[B-37] 當家長的權力抬頭、當教育變成品牌，我們是否仍願意謙虛地承認——所有教育都是實驗？
--------------------------------------------------------------------------------

#19 - Similarity: 0.709 🟡 MODERATE
[A-15] 當我們決意讓孩子浸染在這個語言之下，我們如何思考這個語言和台灣本土文化的關聯？
[B-14] 我們能不能讓孩子在學會外語的同時，也理解母語、理解土地？
--------------------------------------------------------------------------------

================================================================================
ANALYSIS COMPLETE
===============================================================================
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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This means you are free to use, modify, and distribute this software for any purpose, including commercial use, as long as you include the original copyright notice.

## Credits

Built with:
- [Sentence Transformers](https://www.sbert.net/) by UKPLab
- [HuggingFace Transformers](https://huggingface.co/)
- [NumPy](https://numpy.org/)

## Contributing

Feel free to fork, modify, and improve this plagiarism detection system. Suggestions and pull requests are welcome!

---

**Note**: This tool is designed to assist in plagiarism detection but should not be the sole method for determining plagiarism. Human review and judgment are essential for final decisions.

