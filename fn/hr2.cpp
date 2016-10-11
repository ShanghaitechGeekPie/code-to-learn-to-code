/*
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* Reverse(Node* head)
{
    Node* ptr=head;
    if (head!=NULL){
        Node* temp;
        do{
           temp=ptr->next;
           ptr->next=ptr->prev;
           ptr->prev=temp;
           if (temp!=NULL) ptr=temp;
        }while (temp!=NULL);      
    }
    return ptr;
}
