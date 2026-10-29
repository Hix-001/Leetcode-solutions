// 29/10/2026
// Hard
// LeetCode 3841: Palindromic Path Queries in a Tree using Euler Tour and Fenwick BIT.

#include <bits/stdc++.h>
using namespace std;

class Solution {
int n;
vector<int> bit;

void upd(int i, int v) {
    for (; i <= n + 1; i += i & -i) bit[i] ^= v;
}
int qry(int i) const {
    int r = 0;
    for (; i > 0; i -= i & -i) r ^= bit[i];
    return r;
    }

public:
vector<bool> palindromePath(int n_, vector<vector<int>>& edges, string s, vector<string>& queries) {
    n = n_;
    const int LOG = 17;
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
        }

        vector<int> tin(n), tout(n), dep(n, 0);
        vector<array<int, LOG>> up(n);
        vector<int> it(n, 0), stk;
        stk.reserve(n);
        int timer = 0;
        stk.push_back(0);
        tin[0] = ++timer;
        up[0].fill(0);
        while (!stk.empty()) {
            int u = stk.back();
            if (it[u] < (int)adj[u].size()) {
                int v = adj[u][it[u]++];
                if (v == up[u][0] && u != 0) continue;
                if (u == 0 && v == 0) continue;
                dep[v] = dep[u] + 1;
                up[v][0] = u;
                for (int j = 1; j < LOG; ++j) up[v][j] = up[up[v][j - 1]][j - 1];
                tin[v] = ++timer;
                stk.push_back(v);
            } else {
                tout[u] = timer;
                stk.pop_back();
            }
        }

        auto lca = [&](int a, int b) {
            if (dep[a] < dep[b]) swap(a, b);
            int d = dep[a] - dep[b];
            for (int j = 0; j < LOG; ++j)
                if (d >> j & 1) a = up[a][j];
            if (a == b) return a;
            for (int j = LOG - 1; j >= 0; --j) {
                if (up[a][j] != up[b][j]) {
                    a = up[a][j];
                    b = up[b][j];
                }
                }
                return up[a][0];
        };

        bit.assign(n + 3, 0);
        vector<int> mask(n);
        for (int i = 0; i < n; ++i) {
            mask[i] = 1 << (s[i] - 'a');
            upd(tin[i], mask[i]);
            upd(tout[i] + 1, mask[i]);
        }

        vector<bool> ans;
        for (auto& q : queries) {
            istringstream iss(q);
            string type;
            iss >> type;
            if (type == "update") {
                int u;
                char c;
                iss >> u >> c;
                int nm = 1 << (c - 'a');
                int d = mask[u] ^ nm;
                if (d) {
                    upd(tin[u], d);
                    upd(tout[u] + 1, d);
                    mask[u] = nm;
                }
            } else {
                int u, v;
                iss >> u >> v;
                int l = lca(u, v);
                int m = qry(tin[u]) ^ qry(tin[v]) ^ mask[l];
                ans.push_back((m & (m - 1)) == 0);
            }
        }
        return ans;
}
};