# dictditor
Dictionary Editor<br/>
[elhacker.NET](http://www.elhacker.net/)

```
Usage: python dictditor.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -i FILE, --input=FILE
                        Dictionary to modify
  -o PATH, --output=PATH
                        Modified dictionary.
  -r REGEX, --regex=REGEX
                        Regular expression to apply.

```
## Example

`python dictditor.py -i test.txt -o output.txt -r "^[0-9]{2,18}$"`

<table>
<thead>
<tr><th>Input</th><th>Output</th></tr>
</thead>
<tbody>
<tr>
<td>
123<br/>
abc<br/>
3456<br/>
qwr<br/>
12+<br/>
dfq49<br/>
0094j<br/>
78910<br/>
123<br/>
111221123212<br/>
12313232131312321312213312321132132312321132132<br/>
</td>
<td>
123<br/>
3456<br/>
78910<br/>
123<br/>
111221123212<br/>
</td>
</tr>
</tbody>
</tale>
