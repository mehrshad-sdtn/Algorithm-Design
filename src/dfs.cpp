#include <bits/stdc++.h>
using namespace std;

int n = 100;

void dfs_util(vector<int> *adj, int node, int *vis){
    if (vis[node] == 0){
       
        vis[node] = 1;
        cout << node << " -> ";
        for (auto elem: adj[node]) {
            dfs_util(adj, elem, vis);
        }
        
        
    }

}


void dfs(vector<int> *adj, int start){
    int vis[n];
    fill(vis, vis + n, 0);
    dfs_util(adj, start, vis);

    
}
int main(){
    
    vector<int> adj[n];
    cout<<"number of vertices:";
    int num;
    cin >> num;


    for (int i = 0; i < num; i++)
    {
        int u, v;
       cin >> u;
       cin >> v;
       adj[u].push_back(v);
       adj[v].push_back(u);

    }


    cout << "start from? "<<endl;
    int start;
    cin >> start;
    dfs(adj, start);
    cout << "X";
    
}


