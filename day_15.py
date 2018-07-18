    def insert(self,head,data):
        h=Node(data)
        h.next=None
        if head==None:
            head=h
        else :
            c=head
            while c.next:
                c=c.next
            c.next=h
        return head
