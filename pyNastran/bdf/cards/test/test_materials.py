import unittest
import numpy as np
from six.moves import StringIO

from pyNastran.bdf.bdf import BDF, BDFCard, MAT1, MAT8, MAT11
from pyNastran.bdf.field_writer_8 import print_card_8

bdf = BDF(debug=False)

class TestMaterials(unittest.TestCase):
    """tests MAT1"""
    def test_mat1_01(self):
        #
        #MAT5           1    700.    300.    900.    400.    200.    600.     90.+
        #+             .1
        mid = 1
        E = 2e7
        G = 3e7
        nu = 0.4
        rho = 1e-50
        fields = ['MAT1', mid, E, G, nu, rho]

        card = BDFCard(fields)

        mat1 = MAT1.add_card(card)
        self.assertEqual(mid, mat1.Mid())
        self.assertEqual(E, mat1.E())
        self.assertEqual(G, mat1.G())
        self.assertEqual(nu, mat1.Nu())
        self.assertEqual(rho, mat1.Rho())

        size = 8
        msg = mat1.write_card(size, 'dummy')
        self.assertEqual(msg,
                         'MAT1           1    2.+7    3.+7      .4   1.-50\n')

        size = 16
        expected = 'MAT1*                  1       20000000.       30000000.              .4\n*                  1.-50\n'
        actual = mat1.write_card(size, is_double=False)
        msg = 'actual=\n%s\nexpected=\n%s' % (actual, expected)
        self.assertEqual(actual, expected, msg)

    def test_mat1_02(self):
        """tests MAT1, MATT1"""
        model = BDF(debug=False)
        mid = 10
        k = 1000.
        E = 3.0e7
        G = 4.0e6
        nu = 0.2
        mat1 = model.add_mat1(mid, E, G, nu, comment='mat1')
        mat1.write_card(size=16, is_double=False)
        mat1.validate()

        E_table = 1
        G_table = 2
        nu_table = 3
        rho_table = 4
        A_table = 4
        ge_table = 4
        st_table = 4
        sc_table = 4
        ss_table = 4
        matt1 = model.add_matt1(mid, E_table, G_table, nu_table, rho_table,
                                A_table, ge_table, st_table, sc_table, ss_table,
                                comment='matt1')
        matt1.validate()

        x = np.linspace(1., 10.)
        y = np.sin(x) + 5.
        tablem1 = model.add_tablem1(1, x, y, comment='tablem1')
        tablem1.write_card()

        x1 = 1.0
        tablem2 = model.add_tablem2(2, x1, x, y, comment='tablem2')
        tablem2.write_card()

        x2 = 2.0
        tablem3 = model.add_tablem3(3, x1, x2, x, y, comment='tablem3')
        tablem3.write_card()

        #x1 = 1.0
        #x2 = 2.0
        x3 = 3.0
        x4 = 4.0
        a = [5.0]
        tablem4 = model.add_tablem4(4, x1, x2, x3, x4, a, comment='tablem4')
        tablem4.write_card()

        model.validate()
        model.cross_reference()
        model.pop_xref_errors()
        matt1.write_card(size=16, is_double=False)

        read_write(model)

    def test_mat2_01(self):
        """tests MAT2, MATT2"""
        model = BDF(debug=False)
        mid = 10
        G11 = G22 = G12 = G13 = G22 = G23 = G33 = 1.0
        nuxth = nuthz = nuzx = 0.3
        mat2 = model.add_mat2(mid, G11, G12, G13, G22, G23, G33, rho=0.,
                              a1=None, a2=None, a3=None, tref=0.,
                              ge=0., St=None, Sc=None, Ss=None,
                             mcsid=None,
                             comment='')
        mat2.write_card(size=16, is_double=False)
        mat2.validate()

        G11_table = 1
        G12_table = 2
        G13_table = 3
        G22_table = 4
        G23_table = 1
        G33_table = 1
        rho_table = 1
        a1_table = 1
        a2_table = 1
        a3_table = 1
        ge_table = 1
        st_table = 1
        sc_table = 1
        ss_table = 1
        matt2 = model.add_matt2(mid, G11_table, G12_table, G13_table, G22_table,
                                G23_table, G33_table, rho_table,
                                a1_table, a2_table, a3_table,
                                ge_table, st_table, sc_table, ss_table,
                                comment='matt2')
        matt2.validate()

        x = np.linspace(1., 10.)
        y = np.sin(x) + 5.
        tablem1 = model.add_tablem1(1, x, y, comment='tablem1')
        tablem1.write_card()

        x1 = 1.0
        tablem2 = model.add_tablem2(2, x1, x, y, comment='tablem2')
        tablem2.write_card()

        x2 = 2.0
        tablem3 = model.add_tablem3(3, x1, x2, x, y, comment='tablem3')
        tablem3.write_card()

        #x1 = 1.0
        #x2 = 2.0
        x3 = 3.0
        x4 = 4.0
        a = [5.0]
        tablem4 = model.add_tablem4(4, x1, x2, x3, x4, a, comment='tablem4')
        tablem4.write_card()

        model.validate()
        model.cross_reference()
        model.pop_xref_errors()
        matt2.write_card(size=16, is_double=False)
        read_write(model)

    def test_mat3_01(self):
        """tests MAT3"""
        model = BDF(debug=False)
        mid = 10
        ex = 3.0e7
        ey = eth = 6.0e7
        ez = 6e4
        nuxth = nuthz = nuzx = 0.3
        mat3 = model.add_mat3(mid, ex, eth, ez, nuxth, nuthz, nuzx, rho=0.0,
                             gzx=None, ax=0.,
                             ath=0., az=0.,
                             tref=0., ge=0.,
                             comment='mat3')
        mat3.write_card(size=16, is_double=False)
        mat3.validate()

        matt3 = model.add_matt3(
            mid, ex_table=1, eth_table=2, ez_table=3,
            nuth_table=4, nuxz_table=1, rho_table=1,
            gzx_table=1, ax_table=1, ath_table=1,
            az_table=1, ge_table=1, comment='matt3')
        matt3.validate()
        matt3.write_card()

        x = np.linspace(1., 10.)
        y = np.sin(x) + 5.
        tablem1 = model.add_tablem1(1, x, y, comment='tablem1')
        tablem1.write_card()

        x1 = 1.0
        tablem2 = model.add_tablem2(2, x1, x, y, comment='tablem2')
        tablem2.write_card()

        x2 = 2.0
        tablem3 = model.add_tablem3(3, x1, x2, x, y, comment='tablem3')
        tablem3.write_card()

        #x1 = 1.0
        #x2 = 2.0
        x3 = 3.0
        x4 = 4.0
        a = [5.0]
        tablem4 = model.add_tablem4(4, x1, x2, x3, x4, a, comment='tablem4')
        tablem4.write_card()

        model.validate()
        model.cross_reference()
        model.pop_xref_errors()
        #matt3.write_card(size=16, is_double=False)

        read_write(model)

    def test_mat4_01(self):
        """tests MAT4, MATT4"""
        model = BDF(debug=False)
        mid = 10
        k = 1000.
        mat4 = model.add_mat4(mid, k, cp=0.0, rho=1.0, H=None, mu=None,
                              hgen=1.0, ref_enthalpy=None, tch=None, tdelta=None, qlat=None,
                              comment='mat4')
        mat4.write_card(size=16, is_double=False)
        mat4.validate()

        k_table = 1
        cp_table = 2
        H_table = 3
        mu_table = 4
        Hgen_table = 3
        matt4 = model.add_matt4(mid, k_table, cp_table, H_table, mu_table,
                                Hgen_table, comment='matt4')
        matt4.validate()
        matt4.write_card()

        x = np.linspace(1., 10.)
        y = np.sin(x) + 5.
        tablem1 = model.add_tablem1(1, x, y, comment='tablem1')
        tablem1.write_card()

        x1 = 1.0
        tablem2 = model.add_tablem2(2, x1, x, y, comment='tablem2')
        tablem2.write_card()

        x2 = 2.0
        tablem3 = model.add_tablem3(3, x1, x2, x, y, comment='tablem3')
        tablem3.write_card()

        #x1 = 1.0
        #x2 = 2.0
        x3 = 3.0
        x4 = 4.0
        a = [5.0]
        tablem4 = model.add_tablem4(4, x1, x2, x3, x4, a, comment='tablem4')
        tablem4.write_card()

        model.validate()
        model.cross_reference()
        model.pop_xref_errors()
        matt4.write_card(size=16, is_double=False)

        read_write(model)

    def test_mat5_01(self):
        """tests MAT5, MATT5"""
        #
        #MAT5           1    700.    300.    900.    400.    200.    600.     90.+
        #+             .1
        model = BDF(debug=False)
        mid = 10
        mat5 = model.add_mat5(mid, kxx=0., kxy=0., kxz=0., kyy=0., kyz=0.,
                              kzz=0., cp=0.,
                              rho=1., hgen=1., comment='mat5')
        mat5.write_card(size=16, is_double=False)
        mat5.validate()

        kxx_table = 1
        kxy_table = 2
        kxz_table = 3
        kyy_table = 4
        kyz_table = 4
        kzz_table = 4
        cp_table = 4
        hgen_table = 4
        matt5 = model.add_matt5(mid, kxx_table, kxy_table, kxz_table,
                               kyy_table, kyz_table, kzz_table, cp_table, hgen_table,
                               comment='matt5')
        matt5.validate()
        matt5.write_card()

        x = np.linspace(1., 10.)
        y = np.sin(x) + 5.
        tablem1 = model.add_tablem1(1, x, y, comment='tablem1')
        tablem1.write_card()

        x1 = 1.0
        tablem2 = model.add_tablem2(2, x1, x, y, comment='tablem2')
        tablem2.write_card()

        x2 = 2.0
        tablem3 = model.add_tablem3(3, x1, x2, x, y, comment='tablem3')
        tablem3.write_card()

        #x1 = 1.0
        #x2 = 2.0
        x3 = 3.0
        x4 = 4.0
        a = [5.0]
        tablem4 = model.add_tablem4(4, x1, x2, x3, x4, a, comment='tablem4')
        tablem4.write_card()

        model.validate()
        model.cross_reference()
        model.pop_xref_errors()
        matt5.write_card(size=16, is_double=False)

        read_write(model)

    def test_mat8_01(self):  # should fail...
        """tests MAT8"""
        #lines = [  # fails???
        #    'MAT8*    4700007        1675.47         1675.47         .33             *   LHIG',
        #    '*   LHIG28.2            210000.         78000.                          *   LHIH',
        #    '*   LHIH1.32-5          1.32-5          75.             1.943           *   LHII',
        #    '*   LHII1.943           1.943           1.943           3.35',
        #]
        lines = [  # fails
            'MAT8*    4700010        2.83+6          1.14+6          .55             *   LHIJ',
            '*   LHIJ717000.         285194.         285194.                         *   LHIK',
            '*   LHIK9.17-6          2.606-5         70.                             *   LHIL',
            '*   LHIL',
        ]
        lines_expected = [
            'MAT8*            4700010        2830000.        1140000.             .55',
            '*                717000.         285194.         285194.',
            '*              .00000917       .00002606             70.',
            '*',
        ]

        card = bdf.process_card(lines)
        #print(print_card_8(card))
        cardi = BDFCard(card)
        #print("card =", card)
        #with self.assertRaises(RuntimeError):  # temporary RuntimeError
        card2 = MAT8.add_card(cardi)

        fields = card2.raw_fields()
        msg = print_card_8(fields)
        #f = StringIO.StringIO()
        size = 16
        msg = card2.write_card(size, 'dummy')
        #msg = f.getvalue()
        #print(msg)

        lines_actual = msg.rstrip().split('\n')
        msg = '\n%s\n\n%s' % ('\n'.join(lines_expected), msg)
        msg += 'nlines_actual=%i nlines_expected=%i' % (len(lines_actual), len(lines_expected))
        #print(msg)
        self.assertEqual(len(lines_actual), len(lines_expected), msg)
        for actual, expected in zip(lines_actual, lines_expected):
            msg = 'actual   = %r\n' % actual
            msg += 'expected = %r' % expected
            self.assertEqual(actual, expected, msg)

    def test_mat8_02(self):
        """tests MAT8, MATT8"""
        model = BDF(debug=False)
        mid = 10
        e11 = 3.0e7
        e22 = 6.0e7
        nu12 = 0.3
        mat8 = model.add_mat8(mid, e11, e22, nu12)
        mat8.write_card(size=16, is_double=False)
        mat8.validate()

        matt8 = model.add_matt8(
            mid, E1_table=1, E2_table=2, Nu12_table=3,
            G12_table=4, G1z_table=1, G2z_table=1, rho_table=1,
            a1_table=1, a2_table=1,
            xt_table=1, xc_table=1, yt_table=1, yc_table=1,
            s_table=1, ge_table=1, f12_table=1, comment='matt8')
        matt8.validate()
        matt8.write_card()

        x = np.linspace(1., 10.)
        y = np.sin(x) + 5.
        tablem1 = model.add_tablem1(1, x, y, comment='tablem1')
        tablem1.write_card()

        x1 = 1.0
        tablem2 = model.add_tablem2(2, x1, x, y, comment='tablem2')
        tablem2.write_card()

        x2 = 2.0
        tablem3 = model.add_tablem3(3, x1, x2, x, y, comment='tablem3')
        tablem3.write_card()

        #x1 = 1.0
        #x2 = 2.0
        x3 = 3.0
        x4 = 4.0
        a = [5.0]
        tablem4 = model.add_tablem4(4, x1, x2, x3, x4, a, comment='tablem4')
        tablem4.write_card()

        model.validate()
        model.cross_reference()
        model.pop_xref_errors()
        matt8.write_card(size=16, is_double=False)

        read_write(model)

    def test_mat9(self):
        """tests MAT9"""
        model = BDF(debug=False)
        mid = 10
        e11 = 3.0e7
        e22 = 6.0e7
        nu12 = 0.3
        mat9 = model.add_mat9(mid, G11=0., G12=0., G13=0., G14=0., G15=0.,
                             G16=0., G22=0., G23=0., G24=0.,
                             G25=0., G26=0., G33=0., G34=0.,
                             G35=0., G36=0., G44=0., G45=0.,
                             G46=0., G55=0., G56=0., G66=0.,
                             rho=0., A=None, tref=0., ge=0.,
                             comment='mat9')
        mat9.write_card(size=16, is_double=False)
        mat9.validate()

        #matt9 = model.add_matt9
        #matt9.validate()

        model.validate()
        model.cross_reference()
        model.pop_xref_errors()
        #matt8.write_card(size=16, is_double=False)

        read_write(model)

    def test_mat11_01(self):
        """tests MAT11"""
        lines = [
            'MAT11          1    1.+75000000. 700000.      .1     .13     .267000000.+',
            '+       9000000.3000000.      .1    1.-5    7.-6    8.-6     50.',
        ]
        lines_expected = [
            'MAT11          1    1.+75000000. 700000.      .1     .13     .267000000.',
            '        9000000.3000000.      .1  .00001 .000007 .000008     50.'
        ]
        card = bdf.process_card(lines)
        cardi = BDFCard(card)
        card2 = MAT11.add_card(cardi)

        fields = card2.raw_fields()
        msg = print_card_8(fields)
        #f = StringIO.StringIO()
        size = 8
        msg = card2.write_card(size, 'dummy')
        #msg = f.getvalue()
        #print(msg)

        lines_actual = msg.rstrip().split('\n')
        msg = '\n%s\n\n%s' % ('\n'.join(lines_expected), msg)
        msg += 'nlines_actual=%i nlines_expected=%i' % (len(lines_actual), len(lines_expected))
        #print(msg)
        self.assertEqual(len(lines_actual), len(lines_expected), msg)
        for actual, expected in zip(lines_actual, lines_expected):
            msg = '\nactual   = %r\n' % actual
            msg += 'expected =  %r' % expected
            self.assertEqual(actual, expected, msg)

    def test_multiple_materials(self):
        """tests multiple materials"""
        model = BDF(debug=False)
        E = 3.0e7
        G = None
        nu = 0.3
        model.add_mat1(1, E, G, nu)
        e11 = e22 = 3.0e7
        nu12 = 0.3
        model.add_mat8(8, e11, e22, nu12)

        model.add_mat4(4, 10.0)
        model.add_mat5(5)

        bulk = 0.3
        rho = 0.2
        c = None
        model.add_mat10(10, bulk, rho, c)

        structural_material_ids = model.get_structural_material_ids()
        assert len(structural_material_ids) == 3, structural_material_ids

        thermal_material_ids = model.get_thermal_material_ids()
        assert len(thermal_material_ids) == 2, thermal_material_ids

        mats = model.Materials(1)
        assert len(mats) == 1, mats
        mats = model.Materials([1, 4, 5])
        assert len(mats) == 3, mats

        with self.assertRaises(KeyError):
            model.Material(-1)
        with self.assertRaises(KeyError):
            model.StructuralMaterial(-1)
        with self.assertRaises(KeyError):
            model.ThermalMaterial(-1)


def read_write(model):
    """reads/writes the model as a StringIO"""
    bdf_file = StringIO()
    model.write_bdf(out_filename=bdf_file, close=False)
    model.clear_attributes()
    bdf_file.seek(0)
    model.read_bdf(bdf_file, punch=True)
    model.uncross_reference()
    bdf_file.seek(0)
    model.write_bdf(out_filename=bdf_file, size=16, close=False)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
