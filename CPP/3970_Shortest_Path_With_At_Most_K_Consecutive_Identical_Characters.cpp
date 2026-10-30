// 30/10/2026
// Medium
// LeetCode 3970: Shortest Path With At Most K Consecutive Identical Characters using Pareto-pruned State-Space Dijkstra.
#include <vector>
#include <string>
#include <queue>
#include <tuple>

class Solution {
public:
    int shortestPath(int n, std::vector<std::vector<int>>& edges, std::string labels, int k) {
        std::vector<std::vector<std::pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
        }
        
        std::vector<int> min_count(n, 1e9);
        std::priority_queue<std::tuple<int, int, int>, std::vector<std::tuple<int, int, int>>, std::greater<>> pq;
        
        pq.push({0, 0, 1});
        
        while (!pq.empty()) {
            auto [c, u, cnt] = pq.top();
            pq.pop();
            
            if (cnt >= min_count[u]) {
                continue;
            }
            min_count[u] = cnt;
            
            if (u == n - 1) {
                return c;
            }
            
            for (const auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                
                int nxt_cnt = (labels[u] == labels[v]) ? (cnt + 1) : 1;
                
                if (nxt_cnt <= k) {
                    pq.push({c + w, v, nxt_cnt});
                }
            }
        }
        
        return -1;
    }
};