#include <bits/stdc++.h>
using namespace std;

vector<int> bfs_shortest_path(map<int, vector<int>>& graph, int start, int end) {
    unordered_set<int> visited;
    queue<pair<int, vector<int>>> q;
    q.push({start, {start}});
    while (!q.empty()) {
        int vertex = q.front().first;
        vector<int> path = q.front().second;
        q.pop();
        if (vertex == end) {
            return path;
        }
        if (visited.find(vertex) == visited.end()) {
            visited.insert(vertex);
            vector<int> neighbors = graph[vertex];
            for (int neighbor : neighbors) {
                vector<int> new_path = path;
                new_path.push_back(neighbor);
                q.push({neighbor, new_path});
            }
        }
    }
    return {};
}

int main() {
    while (true) {
        try {
            int n, m;
            cin >> n >> m;
            vector<pair<int, int>> edges;
            for (int i = 0; i < m; i++) {
                int ai, bi;
                cin >> ai >> bi;
                edges.push_back({ai, bi});
            }
            map<int, vector<int>> graph;
            for (auto edge : edges) {
                int ai = edge.first;
                int bi = edge.second;
                if (graph.find(ai) == graph.end()) {
                    graph[ai] = {};
                }
                if (graph.find(bi) == graph.end()) {
                    graph[bi] = {};
                }
                graph[ai].push_back(bi);
                graph[bi].push_back(ai);
            }
            int start = 1;
            int end = n;
            vector<int> shortest_path = bfs_shortest_path(graph, start, end);
            cout << shortest_path.size() - 2 << endl;
        } catch (const exception& e) {
            break;
        }
    }
    return 0;
}