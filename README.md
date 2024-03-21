# `trec_arx`

A modification to `treerec` that allows the creation of ".archive.txt" files. These contain all the entries of a directory in a text file, for more manual archiving.

If using the `treerec` repo, the contents of this repo should be placed in `/src/trec_arx`. The module can be called with `import trec_arx`, and the cursor object is called `TreeObj_Cursor()`. 
If using the `treerec` package downloaded from PyPI, then cloning this into a `trec_arx` repo and importing it from the parent file should work just fine.

## Command

The additional command is:

```
   $> new_archive -a "append text" -n "file_name.txt"
```

This creates a new text file, named `file_name.txt` (defaults to `.archive-new.txt`, in the current directory.
The content is a list of all files in the current directory, with each entry followed by "append text" (defaults to empty).
