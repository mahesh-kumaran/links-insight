from webpreview import web_preview, excepts 
from webpreview import OpenGraph
import requests, os


LINK_PREVIEW_ACCESS_KEY = "5dc93469844a9ca355f31b8e517abc70bf477ca77f4ce"
LINK_PREVIEW_URL = "http://api.linkpreview.net/"


# LINK_PREVIEW_ACCESS_KEY = os.environ["LINK_PREVIEW_ACCESS_KEY"]
# LINK_PREVIEW_URL = os.environ["LINK_PREVIEW_URL"]

class LinkParser():

    def __init__(self, url):
        self.url = url 
        
    def parse_using_link_preview(self):

        try: 
            params = {'key': LINK_PREVIEW_ACCESS_KEY, 'q': self.url} 
            response = requests.get(url = LINK_PREVIEW_URL, params = params) 
            if response.status_code == 200: 
                response_data = response.json()
                response_data['parser'] = "link_preview_parser"
                return response_data
            else:
                return { "comment" : "Unable to Access Link Preview Service"}
        except Exception as e: 
            return { "error" : e }

    def parse_using_web(self):

        try :
            url_info = {}
            url_parser['parser'] = "html_parser" 
            title, description, image = web_preview(self.url, parser="html.parser")

            url_info["title"] = title, 
            url_info["description"] = description
            url_info["image"] = image 
            url_info["parser"] = "html_parser" 

            return url_info
        except Exception as e:
            url_info['error'] = e
            return url_info

    def parse_using_og(self):

        try:
            url_info = {}
            url_info['parser'] = "open_graph_parser" 
            og = OpenGraph(self.url, ["og:title", "og:description", "og:image"])

            url_info["title"] = og.title, 
            url_info["description"] = og.description
            url_info["image"] = og.image 
            url_info["parser"] = "open_graph_parser" 

            return url_info
        except Exception as e:
            url_info['error'] = e
            return url_info


def parse_link_information(url):

    
    link_parser = LinkParser(url)
    og_response = link_parser.parse_using_og()

    print(og_response)
    # If Open Graph response is None for Title or description, Try using the web html parser ,
    # If HTML Web parser also fails, Then try using Preview Link    
    if 'title' in og_response and og_response['title'] == None:
        html_response =  link_parser.parse_using_web()
        if html_response['title'] == None: 
            link_preview_response = parse_using_link_preview()
            return link_preview_response
        else: 
            return html_response
    else:
        return og_response 
              
    




