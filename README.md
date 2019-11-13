# links-insight

A simple Flask application that parses a link and returns a JSON which beautifies the simple hyperlink into a previewable. 


Pre-Requisites:

Add the following env variables before starting the app

```sh
export LINK_PREVIEW_ACCESS_KEY = "5dc93469844a9ca355f31b8e517abc70bf477ca77f4ce"
export LINK_PREVIEW_URL = "http://api.linkpreview.net/"
```

Sample API cURL 

```sh
curl -X GET \
  'http://0.0.0.0:5000/link_insight?link=https://gitlab.com/'
```

Sample reponse 

```json

{
  "for_url": "https://gitlab.com/", 
  "response": {
    "description": "\u00e2\u0080\u009cFrom project planning and source code management to CI/CD and monitoring, GitLab is a complete DevOps platform, delivered as a single application. Only GitLab enables Concurrent DevOps to make the 
software lifecycle 200% faster.\u00e2\u0080\u009d", 
    "image": "https://about.gitlab.com/images/blogimages/gitlab-blog-cover.png", 
    "parser": "open_graph_parser", 
    "title": "The first single application for the entire DevOps lifecycle - GitLab"
  }
}
```

