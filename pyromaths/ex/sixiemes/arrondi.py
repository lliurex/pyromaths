#!/usr/bin/env python3

# Pyromaths
# Un programme en Python qui permet de créer des fiches d'exercices types de
# mathématiques niveau collège ainsi que leur corrigé en LaTeX.
# Copyright (C) 2006 -- Jérôme Ortais (jerome.ortais@pyromaths.org)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#
from random import randint, shuffle
import textwrap

from pyromaths import ex
from pyromaths.outils.Affichage import decimaux

precision = [_(u'au millième'), _(u'au centième'), _(u'au dixième'), _(u'à l\'unité'),
             _(u'à la dizaine'), _(u'à la centaine'), _('au millier'),
             _(u'à la dizaine de milliers')]

supinf = ['', _(u' par défaut'), _(u' par excès')]

class ArrondirNombreDecimal(ex.TexExercise):
    """Arrondir des nombres décimaux"""

    tags = ["Sixième"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        hasard = [valide_hasard() for dummy in range(4)]
        choix = [(i, j) for i in range(7)  for j in range(3)]
        shuffle(choix)
        self.choix_precision = [choix[i][0] for i in range(4)]
        self.choix_supinf = [choix[i][1] for i in range(4)]
    # FIXME
        # Arrondir n'est pas synonyme de valeur approchée
        # Valeur approchée par excès 
        # Valeur approchée par défaut 
        # Arrondi = la « meilleure » valeur approchée
        # et ne paraît employé ici correctement
        self.nombres = [hasard[0] / 10 ** (-self.choix_precision[0] + 4),
                        hasard[1] / 10 ** (-self.choix_precision[1] + 4),
                        hasard[2] / 10 ** (-self.choix_precision[2] + 4),
                        hasard[3] / 10 ** (-self.choix_precision[3] + 4)]

    def tex_statement(self):
        exo = ["\\exercice", '\\begin{enumerate}']
        for k in range(4):
            exo.append(_("\\item Arrondir ") + decimaux(self.nombres[k]) + " " + 
                    precision[self.choix_precision[k]] + supinf[self.choix_supinf[k]] + 
                    '.')
        exo.append("\\end{enumerate}")
        return "\n".join(exo)

    def tex_answer(self):
        cor = ["\\exercice*", '\\begin{enumerate}']
        for k in range(4):
            arrondi = round(self.nombres[k], -self.choix_precision[k] + 3)
            if (arrondi > self.nombres[k]):
                defaut = arrondi - 10 ** (self.choix_precision[k] - 3)
                exc = arrondi
            if (arrondi <= self.nombres[k]):
                defaut = arrondi
                exc = arrondi + 10 ** (self.choix_precision[k] - 3)
            if (self.choix_supinf[k] == 0):
                solution = arrondi
            elif (self.choix_supinf[k] == 1):
                solution = defaut
            elif (self.choix_supinf[k] == 2):
                solution = exc
            cor.append(_('\\item L\'encadrement de ') + decimaux(self.nombres[k]) + ' ' + 
                    precision[self.choix_precision[k]] + _(' est :\\par'))
            cor.append(decimaux(defaut) + ' < ' + decimaux(self.nombres[k]) + ' < ' + 
                    decimaux(exc) + '\\par')
            cor.append(_(u'On en déduit que son arrondi ') + 
                    precision[self.choix_precision[k]] + ' ' + supinf[self.choix_supinf[k]] + 
                    _(' est : ') + decimaux(solution) + '.')
        cor.append("\\end{enumerate}")
        return "\n".join(cor)

def valide_hasard():
    """renvoie un nombre float non multiple de 10000"""
    nbre, unite = randint(1000, 100000), randint(1, 9)
    return float(nbre) * 10 + unite
