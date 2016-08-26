# websequencediagrams

python3 version for [websequencediagrams](https://www.websequencediagrams.com/embedding.html)

## Usage

```
python3 convert.py inputFile/inputDir [Style]

```
### Input:
If the input is a directory, it will convert all the files ending with  '.seq'.

Supported Style:

 - default
 - earth
 - magazine
 - modern-blue
 - mscgen
 - napkin
 - omegapple
 - patent
 - qsd
 - rose
 - roundgreen 
 
### Output:
the output files are located at the same postion as the input files. The file names are in the pattern of `<inputFile>.png`