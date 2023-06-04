#include <iostream>
#include <algorithm>
#include <memory.h>
#include <cmath>
#include <vector>
#include <utility>
#include <set>
#include <queue>
#define INF 100000009
using namespace std;

int D[1001];
vector<pair<int, int>> vec[1001];
priority_queue<pair<int, int>> que;
int V, E, K, L, u, v, w;

int func(int K) {
    int min = INF;
    int next, to, weight;

    que.push({0, K});

    while (!que.empty()) {

        int cost = -que.top().first;
        int A = que.top().second;
        que.pop();

        if(D[A]<cost){
            continue;
        }

        for (int i = 0; i < vec[A].size(); i++) {
            to = vec[A][i].first; // v
            weight = vec[A][i].second; //w

            if (D[to] > D[A] + weight) {
                D[to] = D[A] + weight;
                que.push({-D[to], to});
            }
        }
    }

    return 0;
}


int main() {

    cin >> V >> E;

    for(int i = 1; i<=V; i++){
        D[i] = INF;
    }


    for(int i = 0; i<E; i++) {
        cin >> u >> v >> w;
        vec[u].emplace_back(make_pair(v, w));
    }

    cin >> K >> L;
    D[K] = 0;
    func(K);

    cout << D[L];

    return 0;
}