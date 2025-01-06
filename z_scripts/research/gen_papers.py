import json
import glob

def load_papers():
    files = sorted(glob.glob("papers/*.json"))
    papers = []
    for file in files:
        print(file)
        with open(file, 'r') as inp:
            papers.append(json.load(inp))
    return papers

def render_paper(paper):
    render_str = f"<h2>{paper["title"]}</h2>\n"
    render_str += f"<a href='{paper["link"]}'>{paper["link"]}</a><br>\n"
    render_str += f"<div><strong>Abstract: </strong>{paper["abstract"]}</div><br>\n"
    return render_str

def render_papers(papers):
    render_str = ""
    for paper in papers:
        render_str += render_paper(paper) + '\n'
    return render_str

def write_papers(render_str):
    with open('peer-reviewed.html', 'w') as out:
        print(render_str, file=out)

def main():
    papers = load_papers()
    render_str = render_papers(papers)
    write_papers(render_str)

if __name__ == '__main__':
    main()

