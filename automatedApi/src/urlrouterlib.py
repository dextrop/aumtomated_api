from src.read_json_file import read_json_file

class URLRouterLib():
    def __init__(self, requestsObject):
        self.requests = requestsObject
        self.config = read_json_file("ServerData.json")
        self.error_response = {"message": "url not found"}

    def getResponse(self, requested_url, url_conf):
        if (requested_url not in url_conf):
            return self.error_response

        if "json_response" not in url_conf[requested_url]:
            return self.error_response

        return url_conf[requested_url]["json_response"]

    @property
    def get_requests(self):
        if ("GET" not in self.config):
            return self.error_response

        url_conf = self.config["GET"]
        requested_url = str(self.requests.path)[1:]
        return self.getResponse(requested_url, url_conf)

    @property
    def post_requests(self):
        if ("POST" not in self.config):
            return self.error_response

        url_conf = self.config["GET"]
        requested_url = str(self.requests.path)[1:]
        return self.getResponse(requested_url, url_conf)

    @property
    def put_requests(self):
        if ("PUT" not in self.config):
            return self.error_response

        url_conf = self.config["GET"]
        requested_url = str(self.requests.path)[1:]
        return self.getResponse(requested_url, url_conf)

    @property
    def delete_requests(self):
        if ("DELETE" not in self.config):
            return self.error_response

        url_conf = self.config["GET"]
        requested_url = str(self.requests.path)[1:]
        return self.getResponse(requested_url, url_conf)
