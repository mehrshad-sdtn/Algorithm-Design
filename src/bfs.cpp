#include <bits/stdc++.h>
using namespace std;

int n = 100;


void bfs(vector<int> *adj, int start){
    int vis[n];
    fill(vis, vis + n, 0);
    queue<int> q;

    q.push(start);
    vis[start] = 1;
    while(!q.empty()) {
        int node = q.front();
        cout << node << "-> ";
        q.pop();

        for (auto elem: adj[node]){
           if (vis[elem] == 0){
               vis[elem] = 1;
               q.push(elem);
           }
        }
            
             
        
    }

    
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
    bfs(adj, start);
    cout<< "end" ;
    
    
}


