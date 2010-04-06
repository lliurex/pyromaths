# -*- coding: utf-8 -*-

if __name__=="__main__":
    import sys,os
    sys.path.append(os.path.join('..'))

from random import randrange
from classes.Polynome import *
from outils.Polynomes import *
from outils.Affichage import *
from outils.Arithmetique import pgcd

def exo_racines_degre2():
    '''exercice recherche de racines second degré'''

    exo=["\\exercice"]
    cor=["\\exercice*"]
    #intervalle pour les racines entières ou fractionnaire
    rac_min=-10
    rac_max=10
    #denominateur maximmum pour les racines fractionnaires
    denom_max=denom1=12
    #Valeurs absolues maximales des coefficients d'un polynôme quelconque
    abs_a=1
    abs_b=10
    abs_c=10
    #X est le polynome P=x pour faciliter la construction des polynômes,
    inconnues=['x','y','z','t']
    nom_poly=['P','Q','R','S']

    exo.append(u"Résoudre les équations suivantes :")
    cor.append(u"Résoudre les équations suivantes :")
    exo.append("\\begin{enumerate}")
    cor.append("\\begin{enumerate}")
    

    #Racines entières
    nomP='P'
    var=inconnues[randrange(4)]
    X=Polynome({1:1},var)
    P=poly_racines_entieres(rac_min,rac_max,X)

    exo.append("\\item $%s=0$\\par"%(P(var)))
    cor.append("\\item $%s=0$\\par"%(P(var)))
    cor=redaction_racines(P,nomP,var,cor)

    #Racines fractionnaires
    nomP='P'
    var=inconnues[randrange(4)]
    X=Polynome({1:1},var)
    P=poly_racines_fractionnaires(rac_min,rac_max,denom_max,X)
    
    exo.append("\\item $%s=0$\\par"%(P(var)))
    cor.append("\\item $%s=0$\\par"%(P(var)))
    cor=redaction_racines(P,nomP,var,cor)
    
    #Racines quelconques
    nomP='P'
    var=inconnues[randrange(4)]
    X=Polynome({1:1},var)
    P=poly_racines_quelconques(abs_a,abs_b,abs_c,X)
    
    exo.append("\\item $%s=0$\\par"%(P(var)))
    cor.append("\\item $%s=0$\\par"%(P(var)))
    redaction_racines(P,nomP,var,cor)
    
    exo.append("\\end{enumerate}")
    cor.append("\\end{enumerate}")
    return exo,cor

def exo_factorisation_degre2():
    '''exercice recherche de racines second degré'''

    exo=["\\exercice"]
    cor=["\\exercice*"]
    #intervalle pour les racines entières ou fractionnaire
    rac_min=-10
    rac_max=10

    #X est le polynome P(x)=x pour faciliter la construction des polynômes,
    inconnues=['x','y','z','t']
    nom_poly=['P','Q','R','S']

    exo.append(u"Factoriser les polynômes suivants :")
    #cor=[]u"Factoriser les polynômes suivants :"]
    exo.append("\\begin{enumerate}")
    cor.append("\\begin{enumerate}")
    
####identites remarquables
    
    nomP=nom_poly[randrange(4)]
    var=inconnues[randrange(4)]
    X=Polynome({1:1},var)
    P,sgns=poly_id_remarquables(rac_min,rac_max,X)#sgns=-2,0 ou 2
    exo.append(u"\\item Factoriser  $%s(%s)=%s$ à l'aide d'une identité remarquable."% (nomP,var,P(var)))
    cor.append("\\item Factoriser $%s(%s)=%s$"% (nomP,var,P(var)))
               
    factorisation,racines=factorise_identites_remarquables(P,sgns,var,racines=True)
               
    factorise="$$%s"% P
    for i in range(len(factorisation)):
        factorise+="="+factorisation[i]
    cor.append(factorise+"$$")

####Racines entières
    nomP=nom_poly[randrange(4)]
    var=inconnues[randrange(4)]
    X=Polynome({1:1},var)
    P=poly_racines_entieres(rac_min,rac_max,X)
    
    exo.append("\\item $%s(%s)=%s$"%(nomP,var,P(var)))
    cor.append("\\item Factoriser $%s(%s)=%s$\\par"%(nomP,var,P(var)))
    exo,cor=redaction_factorisation(P,nomP,exo,cor)

####Racines fractionnaires
    nomP=nom_poly[randrange(4)]
    var=inconnues[randrange(4)]
    X=Polynome({1:1},var)
    #denominateur maximmum pour les racines fractionnaires
    denom_max=12
    P=poly_racines_fractionnaires(rac_min,rac_max,denom_max,X)

    exo.append("\\item $%s(%s)=%s$"%(nomP,var,P(var)))
    cor.append("\\item Factoriser $%s(%s)=%s$\\par"%(nomP,var,P(var)))
    exo,cor=redaction_factorisation(P,nomP,exo,cor)


####Racines quelconques
    nomP=nom_poly[randrange(4)]
    var=inconnues[randrange(4)]
    X=Polynome({1:1},var)
    #Valeurs absolues maximales des coefficients d'un polynôme quelconque
    abs_a=1
    abs_b=10
    abs_c=10
    P=poly_racines_quelconques(abs_a,abs_b,abs_c,X)
    
    exo.append("\\item $%s(%s)=%s$"%(nomP,var,P(var)))
    cor.append("\\item Factoriser $%s(%s)=%s$\\par"%(nomP,var,P(var)))
    exo,cor=redaction_factorisation(P,nomP,exo,cor)

    exo.append("\\end{enumerate}")
    cor.append("\\end{enumerate}")
    return exo,cor

def exo_factorisation_degre3():
    '''exercice de factorisation degre3'''

    #intervalle pour les racines entières ou fractionnaire
    rac_min=-10
    rac_max=10
    #denominateur maximmum pour les racines fractionnaires
    denom_max=denom1=12
    #Valeurs absolues maximales des coefficients d'un polynôme quelconque
    abs_a=1
    abs_b=10
    abs_c=10
    #X est le polynome P=x pour faciliter la construction des polynômes, TODO : changer  l'inconnue
    inconnues=['x','y','z','t']
    nom_poly=['P','Q','R','S']
    exo=["\\exercice",
        "\\begin{enumerate}"]
    cor=["\\exercice*",
         "\\begin{enumerate}"]
    
    X=Polynome({1:1},var="x")
    E=poly_degre3_racines_entieres(rac_min,rac_max,X)
    exo,cor=factorisation_degre3(E,"E",exo,cor)
    F=poly_degre3_racines_fractionnaires(rac_min,rac_max,denom1,X)
    exo,cor=factorisation_degre3(F,"F",exo,cor)
         
    exo.append("\\end{enumerate}")
    cor.append("\\end{enumerate}")
    return exo,cor

def exo_tableau_de_signe():
    #intervalle pour les racines entières ou fractionnaire
    rac_min=-10
    rac_max=10
    #denominateur maximmum pour les racines fractionnaires
    denom_max=denom1=12
    #Valeurs absolues maximales des coefficients d'un polynôme quelconque
    abs_a=1
    abs_b=10
    abs_c=10
    #X est le polynome P=x pour faciliter la construction des polynômes, TODO : changer  l'inconnue
    inconnues=['x','y','z','t']
    nom_poly=['P','Q','R','S']
    borneinf=float("-inf")
    bornesup=float("inf")
    var="x"
    X=Polynome({1:1},var=var)
    Poly=[poly_racines_entieres(rac_min,rac_max,X),
          poly_racines_fractionnaires(rac_min,rac_max,denom1,X),
          poly_racines_quelconques(abs_a,abs_b,abs_c,X)]

    exo=["\\exercice",
        "\\begin{enumerate}"]
    cor=["\\exercice*",
         "\\begin{enumerate}"]
    nomP="P"
    for i in range(len(Poly)):
        P=Poly[i]
        exo.append(u"\\item Étudier le signe du polynôme $%s=%s$" % (nomP,P))
        cor.append("\\item $%s=%s$\\\\" % (nomP,P))
        delta,simplrac,racines,str_racines,factorisation=factorisation_degre2(P,factorisation=False)
        redaction_racines(P,nomP,var,cor)
        tableau_de_signe(P,nomP,delta,racines,cor,borneinf=float("-inf"),bornesup=float("+inf"),detail=False)
    exo.append("\\end{enumerate}")
    cor.append("\\end{enumerate}")
    return exo,cor

def exo_variation():
    
    exo=["\\exercice",
         "\\begin{enumerate}"]
    cor=["\\exercice*",
         "\\begin{enumerate}"]
    quest1,cor1=quest_fonctions_rationnelles()
    quest2,cor2=quest_variation_degre3(borneinf=-10,bornesup=10)
    quest3,cor3=quest_variation_degre3(borneinf=float("-inf"),bornesup=float("+inf"))
    quest4,cor4=quest_fonctions_rationnelles_sur_R()
    exo+=quest1+quest2+quest3+quest4
    cor+=cor1  + cor2 + cor3 +cor4

    exo.append("\\end{enumerate}")
    cor.append("\\end{enumerate}")
    return exo,cor

def quest_fonctions_rationnelles():
    
    nomf=['f','g','h','k'][randrange(4)]
    var=['t','x'][randrange(2)]
    X=Polynome({1:1},var)
    #intervalle pour les racines entières ou fractionnaire

    rac_min=-9
    rac_max=9
    b1=b2=a1=a2=0
    while b1==0 or b2==0 or a1==0 or a2==0:
        b1=randint(rac_min,rac_max)
        b2=randint(rac_min,rac_max)
        a1=randint(-5,5)
        a2=randint(-5,5)
    P=a1*X+b1
    Q=a2*X+b2

    borneinf=-10
    bornesup=10
    #Je veux que f soit définie et dérivable sur I=Intervalle
    if (-Q[0]/Q[1])>=borneinf and (-Q[0]/Q[1])<=bornesup:
        if ((-Q[0]/Q[1])-borneinf)<(bornesup-(-Q[0]/Q[1])):
            Intervalle=[int(-Q[0]/Q[1])+1,bornesup]
        else:
            Intervalle=[borneinf,int(-Q[0]/Q[1])-1]

    #dérivée
    numerateur="%s\\times%s-%s\\times%s"%(P.derive().TeX(parenthese=True),Q.TeX(parenthese=True),
                                          P.TeX(parenthese=True),Q.derive().TeX(parenthese=True))
    numerateur_simplifie=(P.derive()*Q-P*Q.derive()).simplifie()
    denominateur=u"%s^2"%(Q.TeX(parenthese=True))
    f_derivee="\\dfrac{%s}{%s}"%(numerateur,denominateur)
    f_derivee_simplifiee="\\dfrac{%s}{%s}"%(numerateur_simplifie,denominateur)
    VI=(-Q[0]*Fractions(1)/Q[1]).simplifie()
    exo=[u"\\item On considère la fonction $%s$ définie sur $I=[%s~;~%s]$ par $%s(%s)=\dfrac{%s}{%s}$."%(nomf,Intervalle[0],Intervalle[1],nomf,var,P,Q),
         "\\begin{enumerate}"]
    cor=[u"\\item On considère la fonction $%s$ définie sur $I=[%s~;~%s]$ par $%s(%s)=\dfrac{%s}{%s}$."%(nomf,Intervalle[0],Intervalle[1],nomf,var,P,Q),
         "\\begin{enumerate}"]

    exo.append(u"\\item Justifier que $%s$ est définie et dérivable sur $I$."%(nomf))
    cor.append(u"\\item Justifier que $%s$ est définie et dérivable sur $I$."%(nomf))
    cor.append(u" Pour déterminer la valeur interdite, on doit résoudre $%s=0$."%(Q(var)))
    cor.append("\\begin{align*}")
    cor.append("%s&=0\\\\"% Q)
    cor.append("%s&=%s"%((Q-Q[0]),TeX(-Q[0])))
    cor.append("\\\\")
    if Q[1]!=1:
        x0=-Q[0]*Fractions(1)/Q[1]
        x1=x0.simplifie()
        cor.append("%s&=%s"%(var,TeX(-Q[0]*Fractions(1)/Q[1])))
        cor.append("\\\\")
        if x0.denominateur!=x1.denominateur:
            cor.append("%s&=%s"%(var,TeX(x1)))
            cor.append("\\\\")
    cor.pop(-1)
    cor.append("\\end{align*}")
    cor.append(u"Or $%s$ n'est pas dans l'intervalle $[%s~;~%s]$ et comme $%s$ est un quotient de polynômes, alors $%s$ est définie et dérivable sur $I$."%\
               (TeX(VI),Intervalle[0],Intervalle[1],nomf,nomf))
    exo.append(u"\\item Déterminer $%s'(%s)$ pour tout $%s\in[%s~;~%s]$."%\
          (nomf,var,var,Intervalle[0],Intervalle[1]))
    cor.append(u"\\item Déterminer $%s'(%s)$ pour tout $%s\in[%s~;~%s]$."%\
          (nomf,var,var,Intervalle[0],Intervalle[1]))
    cor.append(u"$$%s'(%s)=%s=%s$$"%(nomf,var,f_derivee,f_derivee_simplifiee))
    exo.append(u"\\item En déduire le sens de variations de $%s$ sur $I$."%(nomf))
    cor.append(u"\\item En déduire le sens de variations de $%s$ sur $I$.\\par"%(nomf))
    if numerateur_simplifie.degre_max==0:
        cor.append(u" Comme $%s$ est un carré, il est toujours positif.\\\\"%(denominateur))
        f_xmin=TeX((Fractions(1)*P(Intervalle[0])/Q(Intervalle[0])).simplifie())
        f_xmax=TeX((Fractions(1)*P(Intervalle[1])/Q(Intervalle[1])).simplifie())
        if numerateur_simplifie[0]<0:
            cor.append(u" De plus, $%s<0$ donc pour tout $%s$ de $I$, $%s'(%s)<0$. Ainsi, on obtient "%\
                  (numerateur_simplifie[0],var,nomf,var))
            cor.append("$$\\tabvar{")
            cor.append("\\tx{%s}&\\tx{%s}&&\\tx{%s}\\cr"%(var,TeX(Intervalle[0]),TeX(Intervalle[1])))
            cor.append("\\tx{%s'(%s)}&&\\tx{-}&&\\cr"%(nomf,var))
            cor.append("\\tx{%s}&\\txh{%s}&\\fd&\\txb{%s}\\cr"%(nomf,f_xmin,f_xmax))
            cor.append("}$$")
        else:
            cor.append(u" De plus, $%s>0$ donc pour tout $%s$ de $I$, $%s'(%s)>0$."%\
                  (numerateur_simplifie[0],var,nomf,var))
            cor.append("$$\\tabvar{")
            cor.append("\\tx{%s}&\\tx{%s}&&\\tx{%s}\\cr"%(var,TeX(Intervalle[0]),TeX(Intervalle[1])))
            cor.append("\\tx{%s'(%s)}&&\\tx{+}&&\\cr"%(nomf,var))
            cor.append("\\tx{%s}&\\txb{%s}&\\fm&\\txh{%s}\\cr"%(nomf,f_xmin,f_xmax))
            cor.append("}$$")
    else:
        cor.append(u" Je ne sais pas faire avec un tel numérateur $%s$."%(numerateur_simplifie))
    exo.append("\\end{enumerate}")
    cor.append("\\end{enumerate}")
    return exo,cor

def quest_fonctions_rationnelles_sur_R():
    
    nomf=['f','g','h','k'][randrange(4)]
    var=['t','x'][randrange(2)]
    X=Polynome({1:1},var)
    #intervalle pour les racines entières ou fractionnaire

    rac_min=-9
    rac_max=9
    b1=b2=a1=a2=0
    while b1==0 or b2==0 or a1==0 or a2==0:
        b1=randint(rac_min,rac_max)
        b2=randint(rac_min,rac_max)
        a1=randint(-5,5)
        a2=randint(-5,5)
    P=a1*X+b1
    Q=a2*X+b2

    borneinf=float("-inf")
    bornesup=float("+inf")
    Intervalle=[borneinf,bornesup]
    TeXintervalle="\\mathbb R"
    
    #dérivée
    numerateur="%s\\times%s-%s\\times%s"%(P.derive().TeX(parenthese=True),Q.TeX(parenthese=True),
                                          P.TeX(parenthese=True),Q.derive().TeX(parenthese=True))
    numerateur_simplifie=(P.derive()*Q-P*Q.derive()).simplifie()
    VI=(-Q[0]*Fractions(1)/Q[1]).simplifie()
    
    denominateur=u"%s^2"%(Q.TeX(parenthese=True))
    f_derivee="\\dfrac{%s}{%s}"%(numerateur,denominateur)
    f_derivee_simplifiee="\\dfrac{%s}{%s}"%(numerateur_simplifie,denominateur)
    
    exo=[u"\\item On considère la fonction $%s$ définie  par $%s(%s)=\dfrac{%s}{%s}$."%(nomf,nomf,var,P,Q),
         "\\begin{enumerate}"]
    cor=[u"\\item On considère la fonction $%s$ définie  par $%s(%s)=\dfrac{%s}{%s}$."%(nomf,nomf,var,P,Q),
         "\\begin{enumerate}"]

    exo.append(u"\\item Déterminer l'ensemble de définition $\\mathcal{D}_{%s}$ de $%s$."%(nomf,nomf))
    cor.append(u"\\item Déterminer l'ensemble de définition $\\mathcal{D}_{%s}$ de $%s$.\par"%(nomf,nomf))
    cor.append(u" La fonction rationnelle $%s$ est définie et dérivable en $%s$ si $%s\\neq0$."%(nomf,var,Q(var))) 
    cor.append("\\begin{align*}\n\
            %s&=0\\\\\n\
            %s&=%s\\\\\n\
            %s&=%s\\\\\n\
            %s&=%s\n\
            \\end{align*}"%(Q,(Q-Q[0]),TeX(-Q[0]),var,TeX(-Q[0]*Fractions(1)/Q[1]),var,TeX(VI)))
    cor.append(u"On en déduit que $\\mathcal{D}_{%s}=\\mathcal{D'}_{%s}=]-\\infty~;~%s[\cup]%s~;~+\\infty[$."%\
          (nomf,nomf,TeX(VI),TeX(VI)))
    exo.append(u"\\item Déterminer $%s'(%s)$ pour tout $%s\in\\mathcal{D'}_{%s}$."%\
          (nomf,var,var,nomf))
    cor.append(u"\\item Déterminer $%s'(%s)$ pour tout $%s\in\\mathcal{D'}_{%s}$."%\
          (nomf,var,var,nomf))
    cor.append(u"$$%s'(%s)=%s=%s$$"%(nomf,var,f_derivee,f_derivee_simplifiee))
    exo.append(u"\\item Dresser le tableau de variations de $%s$ sur $\\mathcal{D}_{%s}$."%(nomf,nomf))
    cor.append(u"\\item Dresser le tableau de variations de $%s$ sur $\\mathcal{D}_{%s}$.\\par"%(nomf,nomf))
    if numerateur_simplifie.degre_max==0:
        cor.append(u" Comme $%s$ est un carré, il est toujours positif.\\\\"%(denominateur))
        f_xmin=TeX((P[1]/Q[1]).simplifie())#TeX((Fractions(1)*P(Intervalle[0])/Q(Intervalle[0])).simplifie())
        f_xmax=f_xmin#TeX((Fractions(1)*P(Intervalle[1])/Q(Intervalle[1])).simplifie())
        if numerateur_simplifie[0]<0:
            cor.append(u" De plus, $%s<0$ donc pour tout $%s$ de $I$, $%s'(%s)<0$. Ainsi, on obtient "%\
                  (numerateur_simplifie[0],var,nomf,var))
            cor.append("$$\\tabvar{")
            cor.append("\\tx{%s}&\\tx{%s}&&&\\tx{%s}&&&\\tx{%s}\\cr"%(var,TeX(Intervalle[0]),TeX(VI),TeX(Intervalle[1])))
            cor.append("\\tx{%s'(%s)}&&\\tx{-}&&\\dbt &&\\tx{-}&\\cr"%(nomf,var))
            cor.append("\\tx{%s}&\\txh{%s}&\\fd&\\txb{-\\infty}&\\dbt&\\txh{+\\infty}&\\fd&\\txb{%s}\\cr"%(nomf,f_xmin,f_xmax))
            cor.append("}$$")
        else:
            cor.append(u" De plus, $%s>0$ donc pour tout $%s$ de $I$, $%s'(%s)>0$."%\
                  (numerateur_simplifie[0],var,nomf,var))
            cor.append("$$\\tabvar{")
            cor.append("\\tx{%s}&\\tx{%s}&&&\\tx{%s}&&&\\tx{%s}\\cr"%(var,TeX(Intervalle[0]),TeX(VI),TeX(Intervalle[1])))
            cor.append("\\tx{%s'(%s)}&&\\tx{+}&&\\dbt&&\\tx{+}&\\cr"%(nomf,var))
            cor.append("\\tx{%s}&\\txb{%s}&\\fm&\\txh{+\\infty}&\\dbt&\\txb{-\\infty}&\\fm&\\txh{%s}\\cr"%(nomf,f_xmin,f_xmax))
            cor.append("}$$")
    else:
        cor.append(u" Je ne sais pas faire avec un tel numérateur $%s$."%(numerateur_simplifie))
    exo.append("\\end{enumerate}")
    cor.append("\\end{enumerate}")
    return exo,cor


def quest_variation_degre3(borneinf=float("-inf"),bornesup=float("+inf")):
    '''Question qui propose l'étude du sens de variation d'un polynôme de degré 3'''
    Intervalle=[borneinf,bornesup]
    if borneinf==float("-inf") and bornesup==float("+inf"):
        TeX_intervalle="\\mathbb R"
    else:
        TeX_intervalle="\\left[%s~;~%s\\right]"%(TeX(borneinf),TeX(bornesup))
    #intervalle pour les racines entières ou fractionnaire
    a=3*randint(1,3)
    rac_min=-9
    rac_max=9
    #denominateur maximmum pour les racines fractionnaires
    denom_max=denom1=12
    #Valeurs absolues maximales des coefficients d'un polynôme quelconque
    abs_a=6
    abs_b=10
    abs_c=10
    #X est le polynome P=x pour faciliter la construction des polynômes, TODO : changer  l'inconnue
    inconnues=['x','y','z','t']
    nom_poly=['P','Q','R','S']
    var="x"
    X=Polynome({1:1},var=var)
    nomP=["f","g","h","k","p","q"][randrange(6)]
    Pprime=poly_racines_entieres(rac_min,rac_max,X,a1=a)
    P=Pprime.primitive()+randint(-abs_c,abs_c)
    P=P.simplifie()
    exo=[u"\\item Étudier le sens de variations de $%s$ définie par $%s(x)=%s$ sur $%s$." % (nomP,nomP,P(var),TeX_intervalle)]
    cor=[u"\\item Étudier le sens de variations de $%s$ définie par $%s(x)=%s$ sur $%s$." % (nomP,nomP,P(var),TeX_intervalle)]
    
    cor.append("\\par $%s'(x)=%s$\\\\" % (nomP,Pprime(var)))
    cor.append(u"Je dois étudier le signe de $%s'(%s)$ qui est un polynôme du second degré.\\par"%(nomP,var))
    
    delta,simplrac,racines,str_racines,factorisation=factorisation_degre2(Pprime,factorisation=False)
    #cor=redaction_factorisation(Pprime,nomP+"'",exo=[],cor=cor)[1]
    #cor.pop(-5)
    redaction_racines(Pprime,nomP+"'",var,cor)
    str_signe=tableau_de_signe(Pprime,nomP+"'",delta,racines,cor,borneinf,bornesup,detail=True)
    #cor.append(tab_signe)

        
    if (delta<=0 and P[3]<0):
        cor+=u"Donc la fonction polynômiale $%s$ est décroissante sur $%s$." %(nomP,TeX_intervalle)
    elif (delta<=0 and P[3]>0):
        cor.append(u"Donc la fonction polynômiale $%s$ est croissante sur $%s$."%(nomP,TeX_intervalle))
    else:
        cor.append("On obtient ainsi le tableau de variation de $%s$."%nomP)
        [x1,x2]=racines
        if P[3]>0:
            var_de_P="\\tx{%s}& \\txb{%s}&\\fm&\\txh{%s}&\\fd&\\txb{%s}&\\fm&\\txh{%s}\\cr"\
                        %(nomP,TeX(P(borneinf)),TeX(P(x1)),TeX(P(x2)),TeX(P(bornesup)))
        else:
            var_de_P="\\tx{%s}& \\txh{%s} &\\fd&\\txb{%s}&\\fm&\\txh{%s}&\\fd&\\txb{%s}\\cr"\
                      %(nomP,TeX(P(borneinf)),TeX(P(x1)),TeX(P(x2)),TeX(P(bornsup)))
        cor.append("$$ \\tabvar{\n \\tx{%s}& \\tx{%s}&& \\tx{%s}&&\\tx{%s}&& \\tx{%s}\\cr\n %s %s}$$"%\
                   (var,TeX(borneinf),TeX(x1),TeX(x2),TeX(bornesup),str_signe,var_de_P))
    return exo,cor


                ###############################################
                #                                             #
                #   Fonctions étudiant les polynômes          #
                #                                             #
                ###############################################

def tableau_de_signe(P,nomP,delta,racines,cor,borneinf=float("-inf"),bornesup=float("+inf"),detail=False):
    '''Étudie le signe d'un polynôme de degré2'''
    ''' ne fonctionne pas si on a pas borneinf < x1< x2 <bornesup'''
    '''detail=True permet de récupérer la dernière ligne avec le signe de P'''
    var=P.var
    signe_moinsa,signe_a=[('+','-'),('-','+')][P[2]>0] #Ca donne bien ce qu'on veut...
    
    if delta<0:
        cor.append("Comme $\\Delta <0$, $%s(%s)$ ne s'annule pas et est toujours du signe de $a$"%(nomP,var))
        cor.append("Ainsi ")
        cor.append("$$\\tabvar{")
        cor.append("\\tx{%s}&\\tx{%s}&& \\tx{%s}\\cr" %(var,TeX(borneinf),TeX(bornesup)))
        str_signe="\\tx{%s(%s)}&&\\tx{%s}&\\cr" %(nomP,var,signe_a)
        cor.append("%s}$$"%(str_signe))

    elif delta == 0:
        cor.append("Comme $\\Delta =0$, $%s(%s)$ s'annule une seule fois pour $%s_0=%s$ et est toujours du signe de $a$.\par"%(nomP,var,var,racines[0]))
        if racines[0]<borneinf or racines[0]>bornesup:
            if borneinf!=float("-inf"):
                intervalle="["
            else:
                intervalle="]"
            intervalle+="%s~;~%s"%(TeX(borneinf),TeX(bornesup))
            if bornesup==float("inf"):
                intervalle+="["
            else:
                intervalle+="]"
            cor.append("Or $%s$ n'est pas dans l'intervalle $%s$ donc"%(TeX(racines[0])))
        else:
            cor.append("$$\\tabvar{")
            cor.append("\\tx{%s}&\\tx{%s}&& \\tx{%s}&& \\tx{%s}\\cr" %(var,TeX(borneinf),TeX(racines[0]),TeX(bornesup)))
            str_signe="\\tx{%s(%s)}&&\\tx{%s}&\\tx{0}&\\tx{%s}&\\cr" %(nomP,var,signe_a,signe_a)
            cor.append("%s}$$"%(str_signe))
    elif delta >0:
        cor.append("Comme $\\Delta >0$, $%s(%s)$ est du signe de $-a$ entre les racines."%(nomP,var))
        compare=[racines[0]<=borneinf+racines[1]<=borneinf,racines[1]>=bornesup+racines[0]>=bornesup]:
        if compare!=[0,0]:
            if borneinf!=float("-inf"):
                intervalle="["
            else:
                intervalle="]"
            intervalle+="%s~;~%s"%(TeX(borneinf),TeX(bornesup))
            if bornesup==float("inf"):
                intervalle+="["
            else:
                intervalle+="]"
            x_x1=x_x2=sign_x1=sign_x2=""
            if compare[0]==1 or compare[1]==2:
                x_x1="&\\tx{%s}&"%(TeX(racines[0]))
                sign_x1="&\\tx{%s}&\\tx{0}"%(signe_a)
            if compare[1]==1 or compare[0]==2:            
                x_x2="&\\tx{%s}&"%(TeX(racines[1]))
                sign_x2="&\\tx{0}&\\tx{%s}"%(signe_a)
        if 2 in compare:
            entreracines="&%s&"%(signe_moinsa)
        else:
            entreracines=&&

        cor.append("Ainsi")
        cor.append("$$\\tabvar{")
        cor.append("\\tx{%s}& \\tx{%s}& %s %s & \\tx{%s}\\cr"%(var,TeX(borneinf),x_x1,x_x2,TeX(bornesup)))
        str_signe="\\tx{%s(%s)}&&\\tx{%s}&\\tx{0}&\\tx{%s}&\\tx{0}&\\tx{%s}&\\cr" %(nomP,var,sign_x1,entreracines,signe_x2)
        cor.append("%s}$$"%(str_signe))
        
    if detail:
        return str_signe

def factorise_identites_remarquables(pol1,sgns,var='',racines=True):
    '''Factorise un polynomes grâce aux identités remarquables'''
    if var=='':
        var=pol1.var
    X=Polynome({1:1},var)
    a1=pgcd(int(pol1[0]),pgcd(int(pol1[1]),int(pol1[2])))#du signe de a=pol1[2]
    if a1!=1 or a1!=-1:
        pol2=pol1/a1
    else:
        pol2=pol1
    #coeff=coeff/int(math.sqrt(a1))
    #pol2=(cx)^2 ±2× cx × b + b^2
    #pol2[2]=c^2
    #pol2[1]=2× cx × b
    #pol2[0] = b^2
    c=int(sqrt(pol2[2]))#problème d'arrondi ?
        
    factorisation=[]
    if a1!=1:
        factorisation.append("%s \\times\\big[ %s \\big]"%(TeX(a1),(pol1/a1).simplifie()))
        facteur2 ="%s\\times \\big["%(TeX(a1))
    else:
        facteur2 =""
    if c!=1:
        facteur2 +=u"(%s %s)^2"%(TeX(c),var)
    else:
        facteur2 +=u"%s^2"% var
    if sgns:
        if sgns==-2: #-2 => (a-b)²
            facteur2 +="-2 \\times "
        else:        #+2 => (a+b)²
            facteur2 +="+2 \\times "
        if c==1:
            facteur2 +=var
        else:
            facteur2 +=TeX(c)+var
        b=int(sqrt(pol2[0]))
        facteur2 +=" \\times %s +"%(TeX(b))
    else:
        #a²-b²
        facteur2 +="-"
        b=int(sqrt(-(pol2[0])))
    facteur2 +=u"%s^2"%(TeX(b))
    if a1!=1:
        facteur2 +="\\big]"
    factorisation.append(facteur2)
    facteur3=""
    if a1!=1:
        facteur3 +=TeX(a1)
    sgns=sgns/2
    if sgns:#(cx-b)² ou (cx+b)²
        liste_racines=[Fractions(-(sgns))*b/c]
        facteur3 +="{(%s)}^2"%(c*X+sgns*b)
    else:#(cx-b)(cx+b)
        liste_racines=[Fractions(-1)*b/c,Fractions(1)*b/c]
        facteur3 +="(%s)(%s)"%(c*X+b,c*X-b)
    factorisation.append(facteur3)
    if racines:
        return factorisation,liste_racines
    return factorisation

def racines_degre2(P):
    """renvoie les racines d'un polynôme de degré 2"""
    delta=int(P[1]**2-4*P[2]*P[0])
    if delta==0:
        x0=Fractions(-1,2)*P[1]/P[2]
        liste_racines=[x0.simplifie()]
        liste_str_racines=["\\dfrac{-%s}{2\\times %s}"%(pTeX(P[1]),pTeX(P[2]))]
        simplrac=[False]
    elif delta>0:
        simplrac,strx1,x1,strx2,x2=listeracines(P[2],P[1],delta,parentheses=False)
        liste_racines=[x1,x2]
        liste_str_racines=[strx1,strx2]
    else:
        simplrac=[False]
        liste_racines=liste_str_racines=[]
    return delta,simplrac,liste_racines,liste_str_racines
    #delta
    #simplrac[0] est True si racine de Delta se simplifie, alors simplrac[1] est la racine de delta simplifiée
    #liste_racines donne la liste des racines sous la forme simplifiée, sous forme numérique si possible
    #liste_str_racine est la liste des racines au format TeX, non simplifié.

def listeracines(a,b,delta,parentheses=False):
    '''renvoie racsimple,simplifie,formule_x1,x_1,formule_x2,x2'''
    '''avec x_1<x_2
       si parenthese=True, renvoie deux booleens 
          parenthesex1=True signifie qu'il faut mettre des parenthese autour de x1
       On suppose delta >0
       simplrac est True si racine de delta se simplifie'''
    a=int(a)
    b=int(b)
    parenthesex1=parenthesex2=True #par défaut
    #simplrac=True
    strx1="\\dfrac{-%s-\\sqrt{%s}}{2\\times %s}"%(pTeX(b),TeX(delta),pTeX(a))
    strx2="\\dfrac{-%s+\\sqrt{%s}}{2\\times %s}"%(pTeX(b),TeX(delta),pTeX(a))
    ##on a strx1<strx2
    coeff,radicande=simplifie_racine(delta)

    #x1,x2 simplifiés ont une écriture fractionnaire donc
    parenthesex1=parenthesex2=False
    if coeff==1:#delta n'a pas de facteur carré, on ne peut rien simplifier
        rac_delta=radicalTeX(delta)
        simplrac=[False]
    else:
        if radicande==1:
            rac_delta=TeX(coeff)
        else:
            rac_delta=TeX(coeff)+radicalTeX(radicande)
        simplrac=[True,rac_delta]
    x1=RacineDegre2(-b,2*a,-1,delta)
    x2=RacineDegre2(-b,2*a,1,delta)
    if b==0:
        parenthesex1=(coeff*a>0)
        parenthesex2=(coeff*a<0)
    if a<0:
        strx1,strx2,x1,x2,parenthesex1,parenthesex2=strx2,strx1,x2,x1,parenthesex2,parenthesex1
    if parentheses:
        return simplrac,strx1,x1,strx2,x2,parenthesex1,parenthesex2
    else:
        return simplrac,strx1,x1,strx2,x2
        #simplrac[0] est True si racine de Delta se simplifie, alors simplrac[1] est la racine de delta simplifiée

def factorisation_degre2(P,factorisation=True):
    #x1=x2=0
    var=P.var
    X=Polynome({1:1},var)
    delta=int(P[1]**2-4*P[2]*P[0])
    if delta<0:
        factorisation=[]
        str_racines=[]
        racines=[]
        simplrac=[False]
    elif delta==0:
        x0=Fractions(-1,2)*P[1]/P[2]
        simplrac=[False]
        racines=[x0.simplifie()]
        str_racines=["\\dfrac{-%s}{2\\times %s}"%(pTeX(P[1]),pTeX(P[2]))]


        P0="%s-%s"%(var,pTeX(racines[0]))
        factorisation=[[P0,P0]]#non simplifiée
        
        if 0>racines[0]:
            P0=X-racines[0]
            factorisation.append([P0,P0])
    else:#delta>0
        simplrac,strx1,x1,strx2,x2=listeracines(P[2],P[1],delta)
        if isinstance(x1,RacineDegre2):
            x1=x1.simplifie()
            x2=x2.simplifie()
        racines=[x1,x2]
        str_racines=[strx1,strx2]
        P1="%s-%s"%(var,pTeX(x1))
        P2="%s-%s"%(var,pTeX(x2))
        factorisation=[[P1,P2]]#non simplifiée
        #Peut-on simplifier les parenthèses ?
        if x1.radicande==0 and (x1.numerateur<0 or x2.numerateur<0):
            P1=(X-x1)(var)
            P2=(X-x2)(var)
            factorisation.append([P1,P2])
    return delta,simplrac,racines,str_racines,factorisation


def factorisation_degre3(E,nomE,exo=[],cor=[],racines=[0,1,-1,2,-2]):
    '''Factorise un polynôme de degré 3 avec une racine évidente'''
    var=E.var
    X=Polynome({1:1},var)
    exo.append("\\item Soit $%s =%s $"%(nomE,E))
    cor.append("\\item Soit $%s=%s $"%(nomE,E))
    exo.append("\\begin{enumerate}")
    cor.append("\\begin{enumerate}")
    exo.append(u"\\item Vérifier si $%s $ possède une racine évidente."%(nomE))
    exo.append("\\item Factoriser $%s $."%(nomE))
    cor.append("\\item ")
    for x0 in racines:
        if E(x0)==0:
            break
    if x0==0:
        degre_facteur=min(E.puiss)
        #degre_facteur=1
        E2=(E/(X**degre_facteur))[0]
        if degre_facteur==1:
            cor.append("On remarque que $%s$ peut se factoriser par $%s$ et $%s=%s\\left(%s\\right)$" %(nomE,var,nomE,var,E2))
        elif degre_facteur==2:
            cor.append(u"On remarque que $%s$ peut se factoriser par $%s^2$ et $%s=%s^2\\left(%s\\right)$"\
            %(nomE,E.var,nomE,E.var,E2))
            exo.append("\\end{enumerate}")
            cor.append("\\end{enumerate}")
            return exo,cor
    else:            
        cor.append("Comme $%s(%s)=0$, on peut diviser $%s$ par $%s$"%(nomE,TeX(x0),nomE,X-x0))
        cor.append(TeX_division(E,(X-x0))+"")
        E2,reste=E/(X-x0)
    cor.append("\\item On doit maintenant factoriser le polynome $%s_2=%s$\\\\"%(nomE,E2))
    delta,simplrac,racines,str_racines,factorisation=factorisation_degre2(E2,factorisation=True)
    cor=redaction_factorisation(E2,nomP=nomE+"_2",exo=[],cor=cor)[1]
    #cor.pop(-5)
    cor.append("\\par")
    cor.append("On en conclue donc que $%s="%(nomE))
    final=0
    if x0==0:
        P0=E.var
    else:
        P0="\\left(%s\\right)"%(X-x0)
    if E[3]==-1:
        cor.append("-")
    elif E[3]!=1:
        cor.append(TeX(E[3]))
    if delta<0:
        P1=factorisation[-1][0]
        E_factorise="%s\\times%s$"%(P0,P1)
    elif delta==0:
        P1=factorisation[-1][0]
        E_factorise="%s\\times{\\left(%s\\right)}^2$"%(P0,P1)
    else:
        
        P1=factorisation[-1][0]
        P2=factorisation[-1][1]
        E_factorise="%s\\left(%s\\right)\\left(%s\\right)$"%(P0,P1,P2)
    cor.append(E_factorise)

    exo.append("\\end{enumerate}")
    cor.append("\\end{enumerate}")
    return exo,cor


#----------------- redaction ---------------------------------------------------------

def redaction_factorisation(P,nomP="P",exo=[],cor=[]):
    var=P.var
    delta,simpl_delta,racines,str_racines,factorisation=factorisation_degre2(P)
    redaction_racines(P,nomP,var,cor)

    #factorisation
    if delta<0:
        cor.append(u"On ne peut pas factoriser $%s(%s)$."%(nomP,var))
    elif delta==0:
        cor.append(u"On peut donc écrire ")
        ligne_factorisation="$$%s(%s)"%(nomP,var)
        for etape in factorisation:
            ligne_factorisation+=" = "
            if P[2]!=1:
                ligne_factorisation+="%s \\times "%(TeX(P[2]))

            ligne_factorisation+="{\\left(%s\\right)}^2"%(etape[0])
        ligne_factorisation+="$$"
        cor.append(ligne_factorisation)
    else:
        cor.append(u"On peut donc écrire ")
        ligne_factorisation="$$%s(%s)"%(nomP,var)
        for etape in factorisation:
            ligne_factorisation+=" = "
            if P[2]!=1:
                ligne_factorisation+="%s \\times "%(TeX(P[2]))
            if len(etape)==1:
                ligne_factorisation+=etape[0]
            else:
                ligne_factorisation+="\\left(%s\\right)\left(%s\\right)"%(etape[0],etape[1])
        ligne_factorisation+="$$"
        cor.append(ligne_factorisation)
    return exo,cor

def redaction_racines(P,nomP,var,cor=[]):
    delta,simpl_delta,liste_racines,liste_str_racines=racines_degre2(P)
    ligne_delta=u"Je calcule $\\Delta=%s^2-4\\times %s\\times %s=%s$"%(pTeX(P[1]),pTeX(P[2]),pTeX(P[0]),TeX(delta))
    if simpl_delta[0]:
        ligne_delta+=" et $%s=%s$.\\par"%(radicalTeX(delta),simpl_delta[1])
    else:
        ligne_delta+=".\\par"
    cor.append(ligne_delta)
    if delta<0:
        cor.append("Comme $\\Delta <0$, $%s(%s)$ n'a pas de racines."%(nomP,var))
    elif delta==0:
        cor.append("Comme $\\Delta=0$, $%s(%s)$ a une seule racine $%s_0=%s=%s$.\\par"%(nomP,var,var,liste_str_racines[0],TeX(liste_racines[0])))
    else:#delta>0
        [x1,x2]=liste_racines
        cor.append("Comme $\\Delta>0$, $%s(%s)$ a deux racines :"%(nomP,var))
        if isinstance(x1,RacineDegre2):
            simplification1=simplification2=""
            x1,detail1=x1.simplifie(True)
            x2,detail2=x2.simplifie(True)
            max_len=max(len(detail1),len(detail2))
            cor.append("\\begin{align*}")
            cor.append("%s =&%s  &%s =&%s"%\
                       (liste_str_racines[0],liste_racines[0],liste_str_racines[1],liste_racines[1]))
            cor.append("\\\\")
            for i in range(0,max_len):
                if i <len(detail1):
                    cor.append("=&%s&"%(detail1[i]))
                else:
                    cor.append("&&")
                if i <len(detail2):
                    cor.append("=&%s"%(detail2[i]))
                else:
                    cor.append("& ")
                cor.append("\\\\")
            cor.pop(-1)
            cor.append("\\end{align*}")
            cor.append("Les racines de $%s$ sont $%s_1=%s$ et $%s_2=%s$."%(nomP,var,x1,var,x2))
        else:
            [strx1,strx2]=liste_str_racines
            cor.append("Les racines de $%s$ sont $%s_1=%s=%s$ et $%s_2=%s=%s$."%(nomP,var,strx1,x1,var,strx2,x2))

    return cor

#######################################
###############TEST####################
#######################################
if __name__=="__main__":
    from TEST.imprimetest import *
    exo,cor=exo_racines_degre2()
##    exof,corf=Exo_factorisation()
##    exof3,corf3=Exo_factorisation_degre3()
##    exo=exor+exof+exof3
##    cor=corr+corf+corf3
##    exo,cor=exo_tableau()
##    exo,cor=exo_variation()
##    exo,cor=exo_fonctions_rationnelles()
##    exo,cor=quest_fonctions_rationnelles_sur_R()
    exo,cor=exo_variation()
##    exo=cor=[]
##    for i in range(10):
##        exo1,cor1=exo_tableau_de_signe()
##        exo=exo+exo1
##        cor=cor+cor1

    imprime_TeX(exo+cor)
