class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        # Your code here

        # If the capacity is greater than the minimum capacity limit
        if capacity > MIN_CAPACITY:
            # Set the intended capacity
            self.capacity = capacity
        # Otherwise, set the capacity to the minimum
        else:
            self.capacity = MIN_CAPACITY
        # Creates an empty hash table at the minimum capacity
        self.hash_data = [None] * self.capacity
        # Keep count of the elements in the hash table
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here

        return len(self.hash_data)


    def get_load_factor(self):
        """
        - Load factor = number of elements stored in the hash table / number of slots
        - Metric to indicate how overfull the hashtable is
        - If linked lists get too long, performance goes down
            - need to shorten the LL
            - add more slots and rehash the table (resize)
            - If the load factor is over 0.7, grow the table
            - If the load factor is under 0.2, shrink the table (down to some minimum)
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here

        return self.count / self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        #!  Your code here
        #? https://gist.github.com/mengzhuo/180cd6be8ba9e2743753

        # Set an original hash value (number of times hashed)
        # 5381 is the traditionally-used value
        hash = 5381

        # Loop through the key
        for x in key:
            # Hash each value
                # hash << 5 = hash value's bits shifted to the left 5 places
                # ord(x) = The integer value representing x's Unicode character
            hash = ((hash << 5) + hash) + ord(x)

        # Return the new hash value at 32 bits
        return hash & 0xFFFFFFFFFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        
        # Set the index of key to a variable
        index = self.hash_index(key)
        # Set the current load factor to a variable
        current_load_factor = self.get_load_factor()

        # If this is an empty list...
        if self.hash_data[index] is None:
            # Store the value in the hash table as a new entry
            self.hash_data[index] = HashTableEntry(key, value)
            # Increase the element counter
            self.count += 1
        else:
            # Reference the current node
            current = self.hash_data[index]
            # Enter while loop: while the current key doesn't match the parameter key
            # and it's not the end of the list...
            while current.key is not key and current.next is not None:
                # Set the current node to current.next to move to the next node (keep checking)
                current = current.next
            # Check if the current key matches the parameter key
            if current.key is key:
                # If so, set the current value to the parameter value
                current.value = value
            # Otherwise, it doesn't match so make a new node
            else:
                # Set the new node to a variable
                new_node = HashTableEntry(key, value)
                # Set the new node's next to the current node
                new_node.next = current
                # Set the current node to the new node
                current = new_node
                # Increase the element counter
                self.count += 1

      
        #? If load factor greater than 0.7...
        
        if current_load_factor > 0.7:
            # Double the hash table size
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        
        # Set the index of key to a variable
        index = self.hash_index(key)
        # Reference current node
        current = self.hash_data[index]
        # Set the current load factor to a variable
        current_load_factor = self.get_load_factor()

        # Check if the current node's key matches the parameter key
        if current.key is key:
            # Check if the current node is at the end of the list
            if current.next:
                # If so, set the current node to None
                current = None
                # Decrease the element counter
                self.count -= 1
            # Otherwise, it's somewhere else and we gotta mess with it's head
            else:
                # Store the current node's next to a variable
                new_head = current.next
                # Now set the current node's next to None
                current.next = None
                # Set the current node to the new head
                current = new_head
                # Decrease the element counter
                self.count -= 1
        # Otherwise, current node's key doesn't match parameter key
        else:
            # Check if the current node is None
            if current is None:
                # Return None
                return None
            # Otherwise, it exists
            else:
                # Set a variable to None to hold the "previous" node's position
                previous = None
                # Enter while loop: while the current key doesn't match the parameter key
                # and it's not the end of the list...
                while current.key is not key and current.next is not None:
                    # Set the previous node to the current node
                    previous = current
                    # Set the current node to it's own next
                    current = current.next
                # If the current key DOES match the parameter key
                if current.key is key:
                    # Set the previous node's next to the current node's next
                    previous.next = current.next
                    # Decrease the element counter
                    self.count -= 1
                    # Return the current value
                    return current.value
                # Otherwise, it wasn't found so return None
                else:
                    return None
                    
        # Catch anything that doesn't hit these other checks
        # Set the value at this index to None
        self.hash_data[index] = None
        # Decrease the element counter
        self.count -= 1

        # Check the load factor
        # Set the new capacity to a variable
        halved_capacity = self.capacity / 2
        # If it's less than 0.2 and the new capacity isn't lower than the minimum
        if current_load_factor < 0.2 and halved_capacity >= MIN_CAPACITY:
            # Half the hash table size
            self.resize(int(halved_capacity))

                



    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here

        # Set the index of key to a variable
        index = self.hash_index(key)
        # Reference current node
        current = self.hash_data[index]

        # If current node is None, value is None
        if current is None:
            return None
        # Else if the current node exists and it's key matches the parameter key
        elif current and current.key is key:
            # Found it! Return the current node's value
            return current.value
        # Otherwise, it exists but the current node's key doesn't match the parameter key
        else:
            # Enter while loop: while the current node's next isn't None
            # And the current node's key doesn't match the parameter key
            while current.next is not None and current.key is not key:
                # Set the current node to it's own next
                current = current.next
            # Return the current value
            return current.value


    def resize(self, new_capacity):
        """
        - Grow = increase performance, shrink = increase memory
        - Grow: double; Shrink: half;
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here

        # Reference the old table
        old_table = self.hash_data[:]
        # Set current capacity to new capacity
        self.capacity = new_capacity
        # Set current hash_data to a new hash table with the new capacity
        self.hash_data = [None] * new_capacity

        # Loop through the range of the old table
        for i in range(len(old_table)):
            # Reference the current node
            current = old_table[i]

            # Check if the current node exists (empty list?)
            if current:
                # Check if the current node's next exists (just one node?)
                if current.next:
                    # Enter while loop: while the next exists (None = end of list)
                    while current.next:
                        # PUT the current node with it's key and value
                        self.put(current.key, current.value)
                        # Set the current node to current.next to move to the next node
                        current = current.next
                    # PUT the final node, now that the while loop is complete
                    self.put(current.key, current.value)
                # If it is only a single node, PUT that single node
                else:
                    self.put(current.key, current.value)



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")