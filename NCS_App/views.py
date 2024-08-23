from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def ncs(request):

    return render(request, 'NCS.html')


def ncs_result(request):

    from ncscode import NCS

    import ast

    class Data:

        def __init__(self, ncs1, ncs2, result):
            
            self.ncs1 = ncs1
            self.ncs2 = ncs2
            self.result = result

    data = []

    if request.method == "POST":

        if request.POST['button'] == 'COMPLEMENT1':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)

                res = ncs1.complement()
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})

        elif request.POST['button'] == 'SCORE1':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1.score()
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})

        elif request.POST['button'] == 'ACCURACY1':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1.accuracy()
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})

        elif request.POST['button'] == 'CERTAINTY1':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1.certainty()
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})

        elif request.POST['button'] == 'COMPLEMENT2':
            
            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs2.complement()
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})

        elif request.POST['button'] == 'SCORE2':
            
            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs2.score()
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})

        elif request.POST['button'] == 'ACCURACY2':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs2.accuracy()
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})

        elif request.POST['button'] == 'CERTAINTY2':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs2.certainty()
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})
        
        elif request.POST['button'] == 'P-UNION':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1.p_union(ncs2)
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})
        
        elif request.POST['button'] == 'EQUALITY':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1 == ncs2
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})
        
        elif request.POST['button'] == 'P-INTERSECTION':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1.p_intersection(ncs2)
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})
        
        elif request.POST['button'] == 'ADDITION':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1 + ncs2
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})
        
        elif request.POST['button'] == 'R-UNION':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1.r_union(ncs2)
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})
        
        elif request.POST['button'] == 'MULTIPLICATION':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1 * ncs2
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})
        
        elif request.POST['button'] == 'R-INTERSECTION':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)

                res = ncs1.r_intersection(ncs2)
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})
        
        elif request.POST['button'] == 'SCALAR MULTIPLICATION':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1.scalar_multiplication(ncs2)
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})
        
        elif request.POST['button'] == 'CONTAINMENT':

            try:
                ncs1 = request.POST['commentsncs1']
                ncs2 = request.POST['commentsncs2']

                request.session['ncs1'] = ncs1
                request.session['ncs2'] = ncs2

                ncs1 = NCS('A', ast.literal_eval(ncs1))

                if not isinstance(ast.literal_eval(ncs2), int):
                    ncs2 = NCS('B', ast.literal_eval(ncs2))
                else:
                    ncs2 = ast.literal_eval(ncs2)
                    
                res = ncs1.containment(ncs2)
            except ValueError:
                res = 'Invalid Input'
            except AttributeError:
                res = 'Invalid Input'
            except TypeError:
                res = 'Invalid Input'

            data.append(Data(ncs1, ncs2, res))

            return render(request, 'NCS_Result.html', {'data' : data})


def ncs_back(request):

    class Data:

        def __init__(self, ncs1, ncs2, result):
            
            self.ncs1 = ncs1
            self.ncs2 = ncs2
            self.result = result

    data = []

    data.append(Data(request.session['ncs1'], request.session['ncs2'], "Result will be displayed here..."))

    return render(request, 'NCS_Back.html', {'data' : data})