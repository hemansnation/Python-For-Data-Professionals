def doc():
    print("""
    dstatistics - all the operations of decriptive stats
    """)

class DesciptiveStatistics:

    def mean(self, l):
        """
        this mean method from DescriptiveStatistics class 
        will print mean of a list.
        """
        return sum(l)/len(l)
    