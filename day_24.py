    def removeDuplicates(self,head):
        l=[]
        ll=[]
        while(head!=None):
            l.append(head.data)
            head=head.next
        head=None
        
        for i in range(len(l)):
            if l[i] not in ll:
                self.insert(head,l[i])
                ll.append(l[i])
        print(*ll)
        return head
