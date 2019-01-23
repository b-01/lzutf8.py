# lzutf8.py
Python implementation of lzutf8.js by rotemdan ([rotemdan/lzutf8.js](https://github.com/rotemdan/lzutf8.js/)). Near 1:1 code transformation from JavaScript to Python. 

I've only implemented the parts that are needed to encode/decode a string. Currently only "SimpleHashTable" has been implemented, as contrary to typical JavaScript use-cases (e.g. web browsers extension), memory usage and execution time is not a problem in Python applications.

## Usage
```python
string = "Test"
compressor = Compressor(customHashTable=CompressorSimpleHashTable)
compressed_string = compressor.compressBlock(string.encode("utf-8"))
```
