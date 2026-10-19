# 08/09/2026
# Medium
# LeetCode 609: Find Duplicate File in System using string parsing and hash map grouping.

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_map = {}
        
        for path_info in paths:
            parts = path_info.split(" ")
            directory = parts[0]
            
            for i in range(1, len(parts)):
                file_info = parts[i]
                open_paren_idx = file_info.index("(")
                
                file_name = file_info[:open_paren_idx]
                content = file_info[open_paren_idx + 1:-1]
                
                full_path = directory + "/" + file_name
                
                if content in content_map:
                    content_map[content].append(full_path)
                else:
                    content_map[content] = [full_path]
                    
        res = []
        for content in content_map:
            if len(content_map[content]) > 1:
                res.append(content_map[content])
                
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))