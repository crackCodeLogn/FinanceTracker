# @author Vivek
# @version 1.0
# @since 27-07-2019
import os

from jinja2 import Template


class HtmlGenerator:
    def __init__(self, caller):
        self.template = Template(open('rd_fd_template.html', 'r').read())
        self.caller = caller

    def generate_html(self, headers, list, total_dep, total_int, maturity):
        html_data = self.template.render(headers=headers, list=list,
                                         total_dep=total_dep,
                                         total_int=total_int,
                                         maturity=maturity)
        self.publish_html(html_data)
        return html_data

    def publish_html(self, data):
        folder = self.create_folder_if_not_existing()
        file = open(folder + self.caller + '_statement.html', 'w')
        file.write(data)
        file.close()

    def create_folder_if_not_existing(self):
        link = os.getcwd() + "/output/"
        if not os.path.exists(link): os.mkdir(link)
        return link
