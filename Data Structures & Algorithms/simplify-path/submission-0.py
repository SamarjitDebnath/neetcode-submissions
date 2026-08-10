class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathList = path.split("/")

        print(pathList)

        for elem in pathList:
            if elem == "..":
                if stack:
                    stack.pop()
            elif elem != "" and elem != ".":
                stack.append(elem)
        
        
        return "/" + "/".join(stack)