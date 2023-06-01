import re
import argparse


def main():
    """
    Convert the awesome diffusion markdown format into HTML.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--fin', type=str, help="input markdown")
    parser.add_argument('--fout', type=str, help="output html")

    args = parser.parse_args()
    html = []

    with open(f'{args.fin}', 'r') as f:
        lines = f.readlines()
        filtered_lines = [line for line in lines if not line.startswith("#")]
        lines = ''.join(filtered_lines)
        all_lines = lines.split('**')
        l = len(all_lines) // 2

        for i in range(0, l):
            title = all_lines[i*2+1]
            rest = all_lines[i*2+2]
            authors = rest.split('\n')[1]
            authors = re.sub(r'\*+', '', authors)
            authors = re.sub(r'\\+', '', authors)
            authors = re.sub(r'<sup>1</sup>', '', authors)
            authors = authors.strip().split(',')
            if len(authors) > 2:
                authors = authors[0].split()[-1] + ' et al.'
            else:
                authors = ' and '.join([a.split()[-1] for a in authors])
            conference = rest.split('\n')[2].split('.')[0].split('(')[0].strip()

            paper_link= rest.split('\n')[2].split('[Paper]')
            if len(paper_link) < 2:
                paper_link = ''
            else:
                paper_link = paper_link[1].split(']')[0][1:-1]
        
            html.append(f'{authors}, <a href="{paper_link}">"{title}"</a>, {conference}<br/>')

    html = '\n'.join(html)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My HTML Page</title>
    </head>
    <body>
    {html}
    </body>
    """

    print(args.fout)

    with open(f'{args.fout}', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    main()