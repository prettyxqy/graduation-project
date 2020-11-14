


class Policy:
  """
  一条政策应该包含：
    政策标题
    政策发布时间
    政策所属类别
    内容
    TODO 可能还有
  """

  def __init__(self) -> None:
    self.metadata = {
      "title": "",
      "time": "",
      "category": ""
    }
    self.content = ""


  def set_metadata(self, **md):
    self.metadata["title"] = md["title"]
    self.metadata["time"] = md["time"]
    self.metadata["category"] = md["category"]

  def set_content(self, content):
    self.content = content

  def __repr__(self) -> str:
    return """
      {
        "title": "%s",
        "time": "%s",
        "category": "%s",
        "content": "%s"
      }
    """ % (self.metadata["title"], self.metadata["time"], self.metadata["category"], self.content)




class PolicyRequest:
  """
  以后可能使用分布式爬虫加快爬取
  """

  def __init__(self, **kwargs) -> None:
    self.title = kwargs['title']
    self.url = kwargs['url']
    self.time = kwargs['time']
    self.category = kwargs['category']
    

  def __repr__(self) -> str:
    return """
      {
        "title": "%s",
        "url": "%s",
        "time": "%s",
        "category": "%s"
      }
    """ % (self.title, self.url, self.time, self.category)


