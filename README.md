# College Projects

A collection of projects built during university coursework. Each folder is a separate project.

## Projects

### Compiler design (`Compiler design/`)
A Streamlit app with two compiler-construction tools:
- **Lexical analyzer** (`lexana.py`): breaks C source code into tokens
- **Intermediate code generator** (`inter.py`): produces three-address code

Sample C programs are included (`program.c`, `programc2.c`, `programc3.c`).

### Financial project (`Financal Project/`)
Stock market prediction combined with news sentiment analysis:
- Notebooks for ARIMA, LSTM/GRU and neural-network sentiment models, plus stock-market prediction
- `Website/`: a Streamlit app that scrapes recent headlines for a ticker, scores their sentiment and predicts the price trend
- Includes the project report (`Report.pdf`) and slides (`PPT.pptx`)

### NLP project (`Nlp Project/`)
A Streamlit app with several NLP tools:
- Mental-healthcare chatbot and COVID-healthcare chatbot (TF-IDF and Linear SVC intent matching)
- Medical condition prediction from drug reviews
- Drug-review sentiment analysis

### SIP project (`SIP_Project/`)
Image-to-image translation: cartoonify, neural style transfer, Deep Dream and Pix2Pix, served through Streamlit. See [`SIP_Project/README.md`](SIP_Project/README.md) for details and sample outputs.

## Getting started

Each project has its own `requirements.txt`. For example:

```bash
cd "Compiler design"
pip install -r requirements.txt
streamlit run app.py
```

## License

See [LICENSE](LICENSE).
