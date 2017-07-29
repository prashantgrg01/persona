import os, sys, requests, bs4

class PaperManager(object):
    def __init__(self, code, year, session, paper_type, paper_num):
        self.baseUrl = "https://papers.gceguide.xyz/A%20Levels"
        self.code = str(code)
        self.year = str(year)
        self.session = str(session)
        self.paper_type = str(paper_type)
        self.paper_num = str(paper_num)

    def get_subject_links(self):
        """
        Returns a list of subject_links of all the paper in papers list
        """
        # download the main page
        mainpage = requests.get(self.baseUrl)
        mainpage.raise_for_status()

        # parse the mainpage to retrive its content
        parsed_mainpage = bs4.BeautifulSoup(mainpage.text, "lxml")

        # retrive all the links which directs to past papers for subjects in our papers list
        subject_anchors = parsed_mainpage.select("td > a")
        subject_links = []
        for anchor in subject_anchors:
            text = anchor.get("href")
            if self.isValidLink(text):
                subject_links.append(self.baseUrl+"/"+text)
        return subject_links

    def get_paper_links(self, subject_links):
        """
        Returns a list of all the pdf links for a given paper
        """
        # for each link we retrieved
        for sublink in subject_links:
            # download the page to which it directs
            subpage = requests.get(sublink)
            subpage.raise_for_status()
            
            # parse the subpage to retrieve its content
            parsed_subpage = bs4.BeautifulSoup(subpage.text, "lxml")
            
            # retrive all the links which is a direct source for a past paper pdf file
            paper_anchors = parsed_subpage.select("td > a")
            paper_links = []
            
            # for each link to the pdf file
            for link in paper_anchors:
                text = link.get("href")
                # check if it is a valid url, if it is then append it to paper_links
                if self.isValidUrl(text):
                    url = sublink+"/"+text
                    name = os.path.basename(url)
                    paper_links.append((name, url))
            return paper_links

    def isValidLink(self, link):
        """ 
        Returns whether the link is valid or not
        i.e. the link is for one of the subject listed in the papers list
        """
        assert type(link) == str, "link must be a string."
        if link.find(self.code) != -1:
            return True
        return False
                
    def isValidUrl(self, url):
        """ 
        Returns whether the url passed is valid or not 
        i.e. it checks whether the file is pdf and so on...
        """
        name = os.path.basename(url)
        if not name.endswith(".pdf"):
            return False
        if name[0:4] != self.code:
            return False
        if self.year != "" and name[6:8] != self.year[2:]:
            return False
        if (self.paper_type != "" and name[9:11] != self.paper_type) or (name[9:11] != "qp" and name[9:11] != "ms"):
            return False
        if self.session != "" and name[5] != self.session:
            return False
        if self.paper_num != "" and name[12] != self.paper_num:
            return False
        return True