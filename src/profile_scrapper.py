from urllib.request import Request, urlopen
from html import unescape


def get_questions(username: str):
    req = Request(
        url = f"https://leetcode.com/{username}/", 
        headers={'User-Agent': 'Mozilla/5.0'}
    ) 
      
    page = urlopen(req)
    html = unescape(page.read().decode("utf-8"))
      
    ques = []
      
    ques_index = html.find("<a class=\"flex h-[56px] items-center rounded px-4")
    while (ques_index != -1):
        html = html[ques_index: ]
        a_tag = html[: html.find("</a>")+4]
        var = "<span class=\"text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium\">"
        a_tag = a_tag[a_tag.find(var)+len(var): ]
        title = a_tag[: a_tag.find("</span>")]
        a_tag = a_tag[len(title)+7: ]
        var = "<span class=\"text-label-3 dark:text-dark-label-3 lc-md:inline hidden whitespace-nowrap\">"
        a_tag = a_tag[a_tag.find(var)+len(var): ]
        time_stamp = a_tag[: a_tag.find("</span>")]
        html = html[len(a_tag): ]
        ques.append((title, time_stamp))
        ques_index = html.find("<a class=\"flex h-[56px] items-center rounded px-4")  

    return [x[0] for x in ques]

if __name__ == "__main__":  
    print(get_questions("lakshay21060"))  
