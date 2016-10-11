int main() {
    int q,t; cin>>q; string s="";
    vector<string> ss; ss.push_back(s);
    for (int i=0; i<q; i++){
        cin>>t;
        switch (t){
            case 1:{
                string w; cin>>w; s=s+w; ss.push_back(s); break;
            }
            case 2:{
                int k; cin>>k;
                for (int i=0; i<k; i++) s.pop_back();
                ss.push_back(s); break;
            }
            case 3:{
                int k; cin>>k; cout<<s[k-1]<<endl; break;
            }
            case 4:{
                s=ss[ss.size()-2]; ss.pop_back(); break;
            }
        }
    }
    return 0;
}
