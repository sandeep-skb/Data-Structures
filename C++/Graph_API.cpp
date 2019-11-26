#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Graph{
  int numNodes;
  unordered_map<int, unordered_set<int>> outgoing;
  unordered_map<int, unordered_set<int>> incoming;
  
public:
  Graph(int numNodes){ this->numNodes= numNodes;}
  void addNode(int );
  void deleteNode(int);
  void addEdge(int, int);
  void deleteEdge(int, int);
  void display_graph();
};

void Graph::addNode(int nodename){
      numNodes++;
      outgoing[nodename] = unordered_set<int> ();
      incoming[nodename] = unordered_set<int> ();
}

void Graph::deleteNode(int node){
  if (outgoing.find(node) == outgoing.end()){
      return;
  }
  
  numNodes--;
  for (auto it=outgoing.begin(); it != outgoing.end(); ++it){
      outgoing[it->first].erase(node);
  }
  outgoing.erase(node);
  
  for (auto it=incoming.begin(); it != incoming.end(); ++it){
      incoming[it->first].erase(node);
  }
  incoming.erase(node);
}


void Graph::addEdge(int src, int dst){
  outgoing[src].insert(dst);
  incoming[dst].insert(src);
}

void Graph::deleteEdge(int src, int dst){
  outgoing[src].erase(dst);
  incoming[dst].erase(src);
}

void Graph::display_graph()
{
    for(auto it=outgoing.begin(); it!=outgoing.end(); ++it){
        cout << it->first << ": [";
        for (auto i : it->second){
            cout << i << " ";
        }
        cout << "]" << endl;
    }
}
int main()
{
    Graph graph(4);
    graph.addEdge(0,1);
    graph.addEdge(0,3);
    graph.addEdge(2,3);
    graph.addEdge(1,2);
    
    graph.display_graph();
    
    cout << "Adding a Node 4" << endl;
    graph.addNode(4);
    graph.display_graph();
    
    cout << "deleting edge (1,2)" << endl;
    graph.deleteEdge(1,2);
    graph.display_graph();
    
    cout << "Adding edge (1,2)" << endl;
    graph.addEdge(1,2);
    graph.display_graph();
    
    return 0;
}
