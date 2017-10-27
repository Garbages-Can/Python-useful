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
