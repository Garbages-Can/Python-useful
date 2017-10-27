<small>markdowntohtml.py</small>
```python
import sys

import argparse
import markdown

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='你的markdown文件名(.md为后缀).')
parser.add_argument('-o', '--output', default='output.html',
                    help='输出的html文件名(.html为后缀),默认名为output.html.')
args = parser.parse_args()

# check arguments:
if not (str(args.filename).endswith('.md') and str(args.output).endswith('.html')):
    print(parser.print_help())
    sys.exit(-1)

with open(args.filename, 'r') as fp:
    text = fp.read()
    print('输入源文件内容:', text, sep='\n')
    html = markdown.markdown(text)
    output_file = args.output
    with open(output_file, 'w') as output:
        print('输出相应的html为:', html, sep='\n')
        output.write(html)

```

将markdown文本转换文html文本

使用方法:

> python3 markdowntohtml.py -f demo.md -o output.html

其中demo.md为你的markdown文件名字, output.html为你想要输出的html文件名子.

你可能需要借助pip安装第三方库:

> pip install markdown