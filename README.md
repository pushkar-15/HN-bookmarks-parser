# HN-bookmarks-parser
A python script to parse bookmarks exported by [Harmonic](https://github.com/SimonHalvdansson/Harmonic-HN) to an Excel file.

## Usage
1. Export bookmarks from the Harmonic application (this creates a `.txt` file named as `HarmonicBookmarks<yyyy-m-d>.txt`) and store the file in the same directory as the script.
2. In the terminal, run `pip install -r requirements.txt` to install the dependencies.
3. Run the python script `main.py` using `python -u <script-path>` (no authentication is required).

A `bookmarks.xlsx` file will be created in the same directory as `main.py`

## Explanation of storage format in the input file is as follows:

Each entry follows this structure:
`<ArticleID>q<Timestamp>`

**ArticleID:**
The part before the `q` is the unique ID of the article/bookmark.
In Hacker News, articles are uniquely identified by numeric IDs (e.g., 36888667).

**Timestamp:**
The part after the `q` is a Unix timestamp in milliseconds.
This timestamp represents the time when the article was bookmarked or when the export was created.

**Delimiter:**
Entries are concatenated with `-`, a separating character between them.