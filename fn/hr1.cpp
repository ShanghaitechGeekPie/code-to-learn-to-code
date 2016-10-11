/*
A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/
bool has_cycle(Node* head) {
    // Complete this function
    // Do not write the main method
    Node* node[100];
    Node* ptr=head;
    int i=0;
    while (ptr!=nullptr){
        for (int j=0; j<i; j++){
            if (ptr==node[j]) return true;
        }
        node[i]=ptr;
        i++;
        ptr=ptr->next;
    }
    return false;   
}
