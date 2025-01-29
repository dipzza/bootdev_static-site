from functools import reduce


class HTMLNode():
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def __eq__(self, other):
    return (
      self.tag == other.tag and
      self.value == other.value and
      self.children == other.children and
      self.props == other.props
    )

  def to_html(self):
    raise NotImplementedError()
  
  def props_to_html(self):
    if self.props is None:
      return ""
    
    html = ""
    for key, value in self.props.items():
      html += f' {key}="{value}"'
    return html
  
  def __repr__(self):
    return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"
  
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def __eq__(self, value):
    return super().__eq__(value)

  def to_html(self):
    if self.value is None:
      raise ValueError()
    
    if self.tag is None:
      return self.value
    
    return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
  
class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("No tag")
    
    if self.children is None:
      raise ValueError("No children")
    
    children_html = ""
    for child in self.children:
      children_html += child.to_html()

    return f"<{self.tag}{super().props_to_html()}>{children_html}</{self.tag}>"