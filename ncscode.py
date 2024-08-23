class INS: # Interval neutrosophic set

    def __init__(self, T_lower = 0, T_upper = 0, I_lower = 0, I_upper = 0, F_lower = 0, F_upper = 0, *args, **kwargs):

        '''Initialising the elements of Interval Neutrosophic Set :-
        Truth (lower,upper), Indeterminacy (lower,upper), Falsehood (lower,upper)
        and handling exceptions'''

        # Handling wrong inputs
        if not 0 <= T_lower <= 1:
            raise ValueError("Invalid Lower Truth value")
        elif not 0 <= T_upper <= 1:
            raise ValueError("Invalid Upper Truth value")
        elif not 0 <= I_lower <= 1:
            raise ValueError("Invalid Lower Indeterminacy value")
        elif not 0 <= I_upper <= 1:
            raise ValueError("Invalid Upper Indeterminacy value")
        elif not 0 <= F_lower <= 1:
            raise ValueError("Invalid Lower Falsehood value")
        elif not 0 <= F_upper <= 1:
            raise ValueError("Invalid Upper Falsehood value")
        elif not T_lower <= T_upper:
            raise ValueError("Lower Truth value cannot be greater \
            than Upper Truth value")
        elif not I_lower <= I_upper:
            raise ValueError("Lower Indeterminacy value cannot be greater \
            than Upper Indeterminacy value")
        elif not F_lower <= F_upper:
            raise ValueError("Lower Falsehood value cannot be greater \
            than Upper Falsehood value")
        elif not 0 <= T_lower+I_lower+F_lower <= 3:
            raise ValueError("Invalid combination of Lower - Truth, \
            Indeterminacy and Falsehood values")
        elif not 0 <= T_upper+I_upper+F_upper <= 3:
            raise ValueError("Invalid combination of Upper - Truth, \
            Indeterminacy and Falsehood values")

        # Initialising
        self._T_lower = T_lower
        self._T_upper = T_upper
        self._I_lower = I_lower
        self._I_upper = I_upper
        self._F_lower = F_lower
        self._F_upper = F_upper
        self._item1 = ([self._T_lower, self._T_upper], [self._I_lower, self._I_upper],
        [self._F_lower, self._F_upper])

        super().__init__(*args, **kwargs)
    # end of the function __init__


    def __str__(self):

        '''For returning the Interval Neutrosophic Set of the form
        A = <[TAl,TAu],[IAl,IAu],[FAl,FAu]>'''

        return f"<[{self._T_lower}, {self._T_upper}],[{self._I_lower},{self._I_upper}],\
        [{self._F_lower},{self._F_upper}]>"
    # end of the function __str__


class NS: # Neutrosophic set

    def __init__(self, truth = 0, indeterminacy = 0, falsehood = 0):

        '''Initialising the NS elements :- Truth, Indeterminacy, Falsehood and handling exceptions'''

        # Handling wrong inputs
        if not 0 <= truth <= 1:
            raise ValueError("Invalid Truth value")
        elif not 0 <= indeterminacy <= 1:
            raise ValueError("Invalid Indeterminacy value")
        elif not 0 <= falsehood <= 1:
            raise ValueError("Invalid Falsehood value")
        elif not 0 <= truth+indeterminacy+falsehood <= 3:
            raise ValueError("Invalid combination of Truth, Indeterminacy and Falsehood values")

        # Initialising
        self._T = truth
        self._I = indeterminacy
        self._F = falsehood
        self._item2 = (self._T, self._I, self._F)
    # end of the function __init__


    def __str__(self):

        '''For returning the NS of the form a=<Tx,Ix,Fx>'''

        return f"<{self._T},{self._I},{self._F}>"
    # end of the function __str__


class NCN(INS, NS): # Neutrosophic cubic number

    def __init__(self, number):

        '''Initialising the Neutrosophic Cubic Number elements :- 
        Truth (lower,upper), Indeterminacy (lower,upper),Falsehood (lower,upper),
        Truth, Indeterminacy, Falsehood and handling exceptions'''

        T_lower, T_upper, I_lower, I_upper, F_lower, F_upper = number[0][0], number[0][1], number[1][0], number[1][1], number[2][0], number[2][1]
        truth, indeterminacy, falsehood = number[3][0], number[3][1], number[3][2]

        super().__init__(T_lower, T_upper, I_lower, I_upper, F_lower, F_upper, truth, indeterminacy, falsehood)
        self._number = number
    # end of the function __init__


    def __len__(self):

        return len(self._number)
    # end of the function __len__


    def __getitem__(self, index):

        return self._number[index]
    # end of the function __getitem__


    def __str__(self):

        '''For returning the Neutrosophic Cubic Number of the form 
        (<[TAl,TAu],[IAl,IAu],[FAl,FAu]>,<Tx,Ix,Fx>)'''

        return f"("+INS.__str__(self)+","+NS.__str__(self)+")"
    # end of the function __str__


    def p_union(self, other):

        return NCN([[max(self._T_lower, other._T_lower), max(self._T_upper, other._T_upper)],
        [max(self._I_lower, other._I_lower), max(self._I_upper, other._I_upper)],
        [max(self._F_lower, other._F_lower), max(self._F_upper, other._F_upper)],
        [max(self._T, other._T), max(self._I, other._I), max(self._F, other._F)]])
    # end of the function p_union


    def p_intersection(self, other):

        return NCN([[min(self._T_lower, other._T_lower), min(self._T_upper, other._T_upper)],
        [min(self._I_lower, other._I_lower),min(self._I_upper, other._I_upper)],
        [min(self._F_lower, other._F_lower),min(self._F_upper, other._F_upper)],
        [min(self._T, other._T),min(self._I, other._I),min(self._F, other._F)]])
    # end of the function p_intersection


    def r_union(self, other):

        return NCN(
        [[max(self._T_lower, other._T_lower), max(self._T_upper, other._T_upper)],
        [max(self._I_lower, other._I_lower), max(self._I_upper, other._I_upper)],
        [max(self._F_lower, other._F_lower), max(self._F_upper, other._F_upper)],
        [min(self._T, other._T), min(self._I, other._I), min(self._F, other._F)]])
    # end of the function r_union


    def r_intersection(self, other):

        return NCN(
        [[min(self._T_lower, other._T_lower), min(self._T_upper, other._T_upper)],
        [min(self._I_lower, other._I_lower), min(self._I_upper, other._I_upper)],
        [min(self._F_lower, other._F_lower), min(self._F_upper, other._F_upper)],
        [max(self._T, other._T), max(self._I, other._I),max(self._F, other._F)]])
    # end of the function r_intersection


    def complement(self):

        return NCN([[round(1-self._T_upper, 2), round(1-self._T_lower, 2)],
        [round(1-self._I_upper, 2), round(1-self._I_lower, 2)],
        [round(1-self._F_upper, 2), round(1-self._F_lower,2)],
        [round(1-self._T, 2), round(1-self._I, 2), round(1-self._F, 2)]])
    # end of the function complement


    def __eq__(self, other):

        '''Checks whether the two Neutrosophic Cubic Numbers are equal or not
        Return value : True or False'''

        return (self._T_lower == other._T_lower) and (self._T_upper == other._T_upper) and \
        (self._I_lower == other._I_lower) and (self._I_upper == other._I_upper) and \
        (self._F_lower == other._F_lower) and (self._F_upper == other._F_upper) and \
        (self._T == other._T) and (self._I == other._I) and (self._F == other._F)
    # end of the function __eq__


    def __add__(self, other):

        return NCN(
        [[round(self._T_lower + other._T_lower - self._T_lower * other._T_lower, 2),
        round(self._T_upper + other._T_upper - self._T_upper * other._T_upper, 2)],
        [round(self._I_lower * other._I_lower, 2),
        round(self._I_upper * other._I_upper, 2)],
        [round(self._F_lower * other._F_lower, 2),
        round(self._F_upper * other._F_upper, 2)],
        [round(self._T + other._T - self._T * other._T, 2),
        round(self._I * other._I, 2),
        round(self._F * other._F, 2)]])
    # end of the function __add__


    def __mul__(self, other):

        return NCN(
        [[round(self._T_lower * other._T_lower, 2),
        round(self._T_upper * other._T_upper, 2)],
        [round(self._I_lower + other._I_lower - self._I_lower * other._I_lower, 2),
        round(self._I_upper + other._I_upper - self._I_upper * other._I_upper, 2)],
        [round(self._F_lower + other._F_lower - self._F_lower * other._F_lower, 2),
        round(self._F_upper + other._F_upper - self._F_upper * other._F_upper, 2)],
        [round(self._T * other._T, 2),
        round(self._I + other._I - self._I * other._I, 2),
        round(self._F + other._F - self._F * other._F, 2)]])
    # end of the function __mul__


    def scalar_multiplication(self, scalar):

        if not scalar > 0:
            raise ValueError("The scalar number should be positive")
        else:
            return NCN([[round(1 - ((1 - self._T_lower) ** scalar), 2), 
            round(1 - ((1 - self._T_upper) ** scalar), 2)],
            [round(self._I_lower ** scalar, 2),round(self._I_upper ** scalar, 2)],
            [round(self._F_lower ** scalar, 2),round(self._F_upper ** scalar, 2)],
            [round(1 - ((1 - self._T) ** scalar), 2),round(self._I ** scalar, 2),round(self._F ** scalar, 2)]])
    # end of the function scalar_multiplication


    def containment(self, other):

        '''Checks whether the first Neutrosophic Cubic Number is a subset
        of the second Neutrosophic Cubic Number
        Return value : True or False'''

        return (self._T_lower < other._T_lower) and (self._T_upper < other._T_upper) and \
        (self._I_lower > other._I_lower) and (self._I_upper > other._I_upper) and \
        (self._F_lower > other._F_lower) and (self._F_upper > other._F_upper) and \
        (self._T < other._T) and (self._I > other._I) and (self._F > other._F)
    # end of the function containment


    def score(self):

        return (round(((6 + self._T_lower + self._T_upper\
        - self._I_lower - self._I_upper\
        - self._F_lower - self._F_upper\
        + self._T - self._I - self._F) / 9), 2))
    # end of the function score


    def accuracy(self):

        return (round((self._T_lower + self._T_upper\
        - self._F_lower - self._F_upper\
        + self._T-self._F), 2))
    # end of the function accuracy


    def certainty(self):

        return (round((self._T_lower + self._T_upper + self._T), 2))
    # end of the function certainty


class NCS(NCN): # Neutrosophic cubic set

    def __init__(self, id_set, item):

        '''Initialising the Neutrosophic Cubic Set elements :- 
        Interval Neutrosophic set and a Neutrosophic set'''

        self._id_set = id_set
        if not isinstance(item, list or tuple):
            raise ValueError("Invalid Neutrosophic Cubic Set")
        self._item = item
    # end of the function __init__


    def __str__(self):

        '''For returning the Neutrosophic Cubic Set of the form
        A = {(<[TAl1,TAu1],[IAl1,IAu1],[FAl1,FAu1]>,<Tx1,Ix1,Fx1>),
        (<[TAl2,TAu2],[IAl2,IAu2],[FAl2,FAu2]>,<Tx2,Ix2,Fx2>)...}'''

        string = f"{self._id_set}"+" = "+"{"
        for i in range(len(self._item)):
            if i < len(self._item) - 1:
                string += f"{NCN(self._item[i])}"+",\n"
            else:
                string += f"{NCN(self._item[i])}"
        string += "}"
        return string
    # end of the function __str__


    def __len__(self):

        return len(self._item)
    # end of the function __len__


    def __getitem__(self, index):

        return self._item[index]
    # end of the function __getitem__


    def p_union(self, other):

        p_union_set = []
        for i in range(len(self._item)):
            p_union_set.append(NCN(self._item[i]).p_union(NCN(other._item[i])))
        return NCS(f"{self._id_set}"+" ∪p "+f"{other._id_set}",p_union_set)
    # end of the function p_union


    def p_intersection(self, other):

        p_intersection_set = []
        for i in range(len(self._item)):
            p_intersection_set.append(NCN(self._item[i]).p_intersection(NCN(other._item[i])))
        return NCS(f"{self._id_set}"+" ∩p "+f"{other._id_set}",p_intersection_set)
    # end of the function p_intersection


    def r_union(self, other):

        r_union_set = []
        for i in range(len(self._item)):
            r_union_set.append(NCN(self._item[i]).r_union(NCN(other._item[i])))
        return NCS(f"{self._id_set}"+" ∪r "+f"{other._id_set}",r_union_set)
    # end of the function r_union


    def r_intersection(self, other):

        r_intersection_set = []
        for i in range(len(self._item)):
            r_intersection_set.append(NCN(self._item[i]).r_intersection(NCN(other._item[i])))
        return NCS(f"{self._id_set}"+" ∩r "+f"{other._id_set}",r_intersection_set)
    # end of the function r_intersection


    def complement(self):

        complement_set = []
        for i in range(len(self._item)):
            complement_set.append(NCN(self._item[i]).complement())
        return NCS(f"{self._id_set}"+"c",complement_set)
    # end of the function complement


    def __eq__(self, other):

        '''Checks whether the two Neutrosophic Cubic sets are equal or not
        Return value : True of False'''

        complement_set = []
        for i in range(len(self._item)):
            complement_set.append(NCN(self._item[i])==NCN(other._item[i]))

        equal = True
        for i in range(len(complement_set)):
            if complement_set[i]==False:
                equal = False

        return equal
    # end of the function __eq__


    def __add__(self, other):

        add_set = []
        for i in range(len(self._item)):
            add_set.append(NCN(self._item[i])+NCN(other._item[i]))
        return NCS(f"{self._id_set}"+" + "+f"{other._id_set}",add_set)
    # end of the function __add__


    def __mul__(self, other):

        mul_set = []
        for i in range(len(self._item)):
            mul_set.append(NCN(self._item[i])*NCN(other._item[i]))
        return NCS(f"{self._id_set}"+" * "+f"{other._id_set}",mul_set)
    # end of the function __mul__


    def scalar_multiplication(self, scalar):

        scalar_mul_set = []
        for i in range(len(self._item)):
            scalar_mul_set.append(NCN(self._item[i]).scalar_multiplication(scalar))
        return NCS(f"{scalar}"+" * "+f"{self._id_set}",scalar_mul_set)
    # end of the function scalar_multiplication


    def containment(self, other):

        '''Checks whether the first Neutrosophic Cubic set is a subset
        of the second Neutrosophic Cubic Number
        Return value : True of False'''

        complement_set = []
        for i in range(len(self._item)):
            complement_set.append(NCN(self._item[i]).containment(NCN(other._item[i])))

        containment=True
        for i in range(len(complement_set)):
            if complement_set[i] == False:
                containment = False
                break

        return containment
    # end of the function containment


    def score(self):

        score_set = []
        for i in range(len(self._item)):
            score_set.append(NCN(self._item[i]).score())

        return score_set
    # end of the function score


    def accuracy(self):

        accuracy_set = []
        for i in range(len(self._item)):
            accuracy_set.append(NCN(self._item[i]).accuracy())

        return accuracy_set
    # end of the function accuracy


    def certainty(self):

        certainty_set = []
        for i in range(len(self._item)):
            certainty_set.append(NCN(self._item[i]).certainty())

        return certainty_set
    # end of the function certainty