import pulp as lp

# PARAMETER
Cvl = {             #Trailer Capacity
    "i1 ke j1" : 23,
    "i1 ke j2" : 25,
    "i2 ke j1" : 23,
    "i2 ke j2" : 25,
        }

Cvt = {             #Truck Capacity
    "jk" : {
        "j1 ke K1" : 10,
        "j1 ke K2" : 12,
        "j1 ke K3" : 10,
        "j1 ke K4" : 12,
        "j2 ke K1" : 10,
        "j2 ke K2" : 12,
        "j2 ke K3" : 10,
        "j2 ke K4" : 12,
    },

    "li" : {
        "l1 ke i1" : 10,
        "l1 ke i2" : 12,
        "l2 ke i1" : 10,
        "l2 ke i2" : 12,
    },

    "lm" : {
        "l1 ke m1" : 10,
        "l1 ke m2" : 12,
        "l2 ke m1" : 10,
        "l2 ke m2" : 12,
    },

    "is" : {
        "i1 ke s1" : 10,
        "i1 ke s2" : 12,
        "i1 ke s3" : 10,
        "i1 ke s4" : 12,
        "i2 ke s1" : 10,
        "i2 ke s2" : 12,
        "i2 ke s3" : 10,
        "i2 ke s4" : 12,
    },
    
    "sl" : {
        "s1 ke l1" : 10,
        "s2 ke l1" : 12,
        "s3 ke l1" : 10,
        "s4 ke l1" : 12,
        "s1 ke l2" : 10,
        "s2 ke l2" : 12,
        "s3 ke l2" : 10,
        "s4 ke l2" : 12,
    }
}

Cdv = { # Asumsi Trailer Petrol dan Truck Petrol
    "ij" : {
        "i1 ke j1" : 4,
        "i1 ke j2" : 5,
        "i2 ke j1" : 4,
        "i2 ke j2" : 5,
    },

    "jk" : {
        "j1 ke K1" : 9,
        "j1 ke K2" : 10,
        "j1 ke K3" : 9,
        "j1 ke K4" : 10,
        "j2 ke K1" : 9,
        "j2 ke K2" : 10,
        "j2 ke K3" : 9,
        "j2 ke K4" : 10,
    },

    "li" : {
        "l1 ke i1" : 9,
        "l1 ke i2" : 10,
        "l2 ke i1" : 9,
        "l2 ke i2" : 10,
    },

    "lm" : {
        "l1 ke m1" : 9,
        "l1 ke m2" : 10,
        "l2 ke m1" : 9,
        "l2 ke m2" : 10,
    },

    "is" : {
        "i1 ke s1" : 9,
        "i1 ke s2" : 10,
        "i1 ke s3" : 9,
        "i1 ke s4" : 10,
        "i2 ke s1" : 9,
        "i2 ke s2" : 10,
        "i2 ke s3" : 9,
        "i2 ke s4" : 10,
    },
    
    "sl" : {
        "s1 ke l1" : 9,
        "s2 ke l1" : 10,
        "s3 ke l1" : 9,
        "s4 ke l1" : 10,
        "s1 ke l2" : 9,
        "s2 ke l2" : 10,
        "s3 ke l2" : 9,
        "s4 ke l2" : 10,
    }
}

d = {
    "ij" : {
        "i1 ke j1" : 150,
        "i1 ke j2" : 500,
        "i2 ke j1" : 150,
        "i2 ke j2" : 500,
    },
    
    "jk" : {
        "j1 ke K1" : 100,
        "j1 ke K2" : 350,
        "j1 ke K3" : 100,
        "j1 ke K4" : 350,
        "j2 ke K1" : 100,
        "j2 ke K2" : 350,
        "j2 ke K3" : 100,
        "j2 ke K4" : 350,
    },

    "kl" : {
        "k1 ke l1" : 90,
        "k1 ke l2" : 100,
        "k2 ke l1" : 90,
        "k2 ke l2" : 100,
        "k3 ke l1" : 90,
        "k3 ke l2" : 100,
        "k4 ke l1" : 90,
        "k4 ke l2" : 100,
    },

    "li" : {
        "l1 ke i1" : 200,
        "l1 ke i2" : 650,
        "l2 ke i1" : 200,
        "l2 ke i2" : 650,
    },

    "lm" : {
        "l1 ke m1" : 250,
        "l1 ke m2" : 750,
        "l2 ke m1" : 250,
        "l2 ke m2" : 750,
    },

    "is" : {
        "i1 ke s1" : 110,
        "i1 ke s2" : 125,
        "i1 ke s3" : 110,
        "i1 ke s4" : 125,
        "i2 ke s1" : 110,
        "i2 ke s2" : 125,
        "i2 ke s3" : 110,
        "i2 ke s4" : 125,
    },

    "sl" : {
        "s1 ke l1" : 150,
        "s2 ke l1" : 200,
        "s3 ke l1" : 150,
        "s4 ke l1" : 200,
        "s1 ke l2" : 150,
        "s2 ke l2" : 200,
        "s3 ke l2" : 150,
        "s4 ke l2" : 200,
    }
}

# MANUFACTURE COST

PCi = {
    "Manufaktur 1" : 12.5,
    "Manufaktur 2" : 19.5
}

Cre = {
    "Manufaktur 1" : 8,
    "Manufaktur 2" : 13
}

Beta = {
    "Manufaktur 1" : 0.1,
    "Manufaktur 2" : 0.3
}

Pngi = {
    "Manufaktur 1" : 50,
    "Manufaktur 2" : 55
}

q = {
    "Manufaktur 1" : 0.3,
    "Manufaktur 2" : 0.5
}

b = {
    "Manufaktur 1" : 0.1,
    "Manufaktur 2" : 0.3
}

dd = {
    "Manufaktur 1" : 0.3,
    "Manufaktur 2" : 0.5
}

# SECONDARY MARKET
Csr = {
    "Sekunder 1" : 30,
    "Sekunder 2" : 35,
    "Sekunder 3" : 45,
    "Sekunder 4" : 50,
}


# DISTRIBUTOR COST

Coj = {
    "Distributor 1" : 5,
    "Distributor 2" : 8
}

# COLLECTOR COST

Ccl = {
    "Collector 1" : 13,
    "Collector 2" : 17
}

Fcl = {
    "Collector 1" : 20*20,
    "Collector 2" : 20*25
}

# DISPOSER COST

Cdl = {
    "Disposer 1" : 10,
    "Disposer 2" : 13
}

Fbm = {
    "Disposer 1" : 10*30,
    "Disposer 2" : 10*35
}

# CAPACITY 
Cppi ={
    "Manufaktur 1" : 135,
    "Manufaktur 2" : 150
}

Cri = {
    "Manufaktur 1" : 88,
    "Manufaktur 2" : 92
}

Cpdj = {
    "Distributor 1" : 50,
    "Distributor 2" : 60   
}

Cccl = {
    "Collector 1" : 70,
    "Collector 2" : 95
}

Ccdm = {
    "Disposer 1" : 80,
    "Disposer 2" : 100
}

# DEMAND
Dk = {
    "Konsumen 1" : 100,
    "Konsumen 2" : 110,
    "Konsumen 3" : 120,
    "Konsumen 4" : 130
}

Ds = {
    "Sekunder 1" : 25,
    "Sekunder 2" : 35,
    "Sekunder 3" : 45,
    "Sekunder 4" : 50,
}

# Kumpulan Keys
manuf_keys = PCi.keys()
distributor_keys = Coj.keys()
konsumen_keys = Dk.keys()
sekunder_keys = Ds.keys()
collector_keys = Cccl.keys()
disposer_keys = Ccdm.keys()
Cdv_ij = Cdv["ij"].keys()
Cdv_jk = Cdv["jk"].keys()
Cdv_li = Cdv["li"].keys()
Cdv_lm = Cdv["lm"].keys()
Cdv_is = Cdv["is"].keys()
Cdv_sl = Cdv["sl"].keys()
d_ij = d["ij"].keys()
d_jk = d["jk"].keys()
d_kl = d["kl"].keys()
d_li = d["li"].keys()
d_lm = d["lm"].keys()
d_is = d["is"].keys()
d_sl = d["sl"].keys()
Cvl_keys = Cvl.keys()
Cvt_keys_jk = Cvt["jk"].keys()
Cvt_keys_li = Cvt["li"].keys()
Cvt_keys_lm = Cvt["lm"].keys()
Cvt_keys_is = Cvt["is"].keys()
Cvt_keys_sl = Cvt["sl"].keys()

# Model Problem
problem = lp.LpProblem("Supply_Chain_Optimization", lp.LpMinimize)

# Variabel Manufaktur
PMi = lp.LpVariable.dicts("jumlah_produksi_manuf", manuf_keys, 0,None,cat=lp.LpInteger)
Pd = lp.LpVariable.dicts("penawaran_diskon", manuf_keys, 0,None,cat=lp.LpInteger)
Pre = lp.LpVariable.dicts("nilai_bekas_pakai", manuf_keys, 0,None,cat=lp.LpInteger)
QPij = lp.LpVariable.dicts("jumlah_produk_yang_diproduksi", manuf_keys, 0,None,cat=lp.LpInteger)
Qrli = lp.LpVariable.dicts("jumlah_produk_remanufaktur", manuf_keys, 0,None,cat=lp.LpInteger)
GLti = lp.LpVariable.dicts("parameter_ramah", manuf_keys, 0, 1,cat=lp.LpInteger)

# Variabel Distributor
Qdjk = lp.LpVariable.dicts("produk_to_konsum",konsumen_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# Variabel Konsumen
Rkl =  lp.LpVariable.dicts("konsumen_to_collector",collector_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# Variabel Sekunder
Qmis =  lp.LpVariable.dicts("produk_ke_pasar_sekunder",sekunder_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# Variabel Collector
Ul = lp.LpVariable.dicts("parameter_bangun_collector", collector_keys, 0,1,cat=lp.LpBinary)
Qwsl =  lp.LpVariable.dicts("produk_ke_pusat_pengumpulan",collector_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# Variabel Disposer
Vm = lp.LpVariable.dicts("parameter_bangun_disposer", disposer_keys, 0,1,cat=lp.LpBinary)
Qslm =  lp.LpVariable.dicts("produk_dibuang",disposer_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# KALKULASI BIAYA

# Kalkulasi Biaya Manufaktur Cpi = PCi + Beta * GLti
for item1 in manuf_keys :
    for item2 in manuf_keys:
        for item3 in manuf_keys: 
            if GLti[item1] != 0 : 
                biaya_produksi = lp.lpSum((PCi[item1] + Beta[item2]) * QPij[item3]) 
            if GLti[item1] == 0 : 
                biaya_produksi = lp.lpSum(PCi[item1] * QPij[item3]) 

# Kalkulasi Biaya Remanufaktur, Cre * QRli --> Ngga Pengaruh Ke Total Biaya
# for item1 in manuf_keys:
#     for item2 in manuf_keys: 
#         biaya_remanufaktur = lp.lpSum(Cre[item1] * Qrli[item2])

# Kalkulasi Biaya Pengiriman I ke J --> Belum Dibagi Kapasitas Cvr atau Cvt --> Pengaruh ke Total Biaya
# for item in Cdv_ij :
#     for item2 in distributor_keys :
#         for item3 in d_ij :
#             biaya_pengiriman_i_j = Cdv["ij"][item] * QPij[item2] * d["ij"][item3]

# Kalkulasi Biaya Diskon Qrli * Pd * Dd --> Ini gabisa di eksekusi karena Qrli dan Pd merupakan variable tidak konstan
# for item1 in manuf_keys :
#     for item2 in manuf_keys :
#         for item3 in manuf_keys :
#             biaya_diskon = lp.lpSum(Qrli[item1]*dd[item3]*Pd[item2])

# Kalkulasi Biaya Penanganan di Distributor Coj * Qdjk --> Ngga Pengaruh Ke Total Biaya
# for item in distributor_keys :
#     for item2 in konsumen_keys :
#         biaya_penanganan = lp.lpSum(Coj[item] * Qdjk[item2])

# Kalkulasi Biaya Pengiriman J ke K --> Belum Dibagi Kapasitas Cvr atau Cvt --> Ngga Pengaruh Ke Total Biaya
# for item in Cdv_jk :
#     for item2 in konsumen_keys :
#         for item3 in d_jk :
#             biaya_pengiriman_j_k = Cdv["jk"][item] * Qdjk[item2] * d["jk"][item3]

# Kalkulasi Fixed Cost Capacity Collector Fcl Ul --> Ngga Pengaruh Ke Total Biaya
# for item in collector_keys :
#     for item2 in collector_keys :
#         if Ul[item2] != 0 :
#             fixed_cost_collector = lp.lpSum(Fcl[item]) * 1
#         if Ul[item2] == 0 :
#             fixed_cost_collector = 0

# Kalkulasi Biaya Pemilahan Ccl Rkl --> Ngga Pengaruh Ke Total Biaya
for item in collector_keys :
    for item2 in collector_keys :
        biaya_pemilahan = lp.lpSum(Ccl[item] * Rkl[item2])

# Fungsi Tujuan
problem += lp.lpSum(biaya_produksi )

# Constraint
#QPij >= Dk --> Aman
for item1 in manuf_keys :
    for item2 in konsumen_keys :
        problem += lp.lpSum(QPij[item1]) >= lp.lpSum(Dk[item2])

#Qmis >= Ds
for item1 in sekunder_keys:
    for item2 in sekunder_keys :
        problem += lp.lpSum(Qmis[item1]) >= lp.lpSum(Ds[item2])

#Qdjk <= QPij
for item in konsumen_keys:
    for item2 in manuf_keys:
        problem += lp.lpSum(Qdjk[item]) <= lp.lpSum(QPij[item2])

#QRli <= (1-Fd) Rkl
for item in manuf_keys :
    for item2 in collector_keys:
        problem += lp.lpSum(Qrli[item]) <= (1-0.5) * lp.lpSum(Rkl[item2])

#QSlm == Fd Rkl + Qwsl
for item in disposer_keys :
    for item2 in collector_keys :
        for item3 in collector_keys : 
            problem += lp.lpSum(Qslm[item]) == 0.5 * lp.lpSum(Rkl[item2]) + lp.lpSum(Qwsl[item3])

#Rkl <= Yk QDjk GLti --> Yk belum terkonversi
for item in collector_keys:
    for item2 in konsumen_keys:
        for item3 in manuf_keys :
            if GLti[item3] != 0 :
                problem += 0.5 * lp.lpSum(Rkl[item]) <= lp.lpSum(Qdjk[item2])
            if GLti[item3] == 0 :
                problem += lp.lpSum(Rkl[item]) == 0
                
#QRli <= Qpij
for item in manuf_keys:
    for item2 in manuf_keys:
        problem += lp.lpSum(Qrli[item]) <= lp.lpSum(QPij[item2])

#Qmis <= Qrli
for item in sekunder_keys:
    for item2 in manuf_keys:
        problem += lp.lpSum(Qmis[item]) <= lp.lpSum(Qrli[item2])

#Qwsl <= Qmis
for item in collector_keys:
    for item2 in sekunder_keys :
        problem += lp.lpSum(Qwsl[item]) <= lp.lpSum(Qmis[item2])

#Qpij <= Cppi
for item in manuf_keys :
    for item2 in manuf_keys:
        problem += lp.lpSum(QPij[item]) <= lp.lpSum(Cppi[item2])

#Qdjk <= Cpdj
for item in konsumen_keys:
    for item2 in distributor_keys :
        problem += lp.lpSum(Qdjk[item]) <= lp.lpSum(Cpdj[item2])

#Rkl <= ul Cccl  --> Ditambahkan Langkah Logis nya untuk menentukan Ul (Based on 0 < RKL < Cccl, maka collector +1 )
for item in collector_keys : 
    for item2 in collector_keys :
        if Ul[item2] != 0 :
            problem += lp.lpSum(Rkl[item]) <= lp.lpSum(Cccl[item2])
        if Ul[item2] == 0 :
            problem += lp.lpSum(Rkl[item]) == 0

#Qwsl <= ul Csrl --> Ditambahkan Langkah Logis nya untuk menentukan Ul (Based on 0 < RKL < Cccl, maka collector +1 )
for item in collector_keys:
    for item2 in sekunder_keys:
        for item3 in collector_keys: 
            if Ul[item3] != 0 :
                problem += lp.lpSum(Qwsl[item]) <= lp.lpSum(Csr[item2])
            if Ul[item3] == 0 :
                problem += lp.lpSum(Qwsl[item]) == 0 
                
#Qrli <= Cri --> Ditambahkan Langkah Logis nya untuk menentukan Ul (Based on 0 < RKL < Cccl, maka collector +1 )
for item in manuf_keys :
    for item2 in manuf_keys:
        problem += lp.lpSum(Qrli[item]) <= lp.lpSum(Cri[item2])

#Qslm <= vm Ccdm
for item in disposer_keys :
    for item2 in disposer_keys :
        if Vm[item2] != 0 :
            problem += lp.lpSum(Qslm[item]) <= lp.lpSum(Ccdm[item2])
        if Vm[item2] == 0 :
            problem += lp.lpSum(Qslm[item]) == 0

#Pd <= Pngi
for item in manuf_keys :
    for item2 in manuf_keys:
        problem += lp.lpSum(Pd[item]) <= lp.lpSum(Pngi[item2])

# EV1
for item in d_ij :
    for item2 in manuf_keys:
        for item3 in Cvl_keys :
            for item4 in d_is :
                for item5 in sekunder_keys :
                    for item6 in Cvt_keys_is :            
                        problem += 50 * (lp.lpSum(d["ij"][item] * (QPij[item2] * (Cvl[item3])**-1)) + lp.lpSum(d["is"][item4] * (Qmis[item5] * (Cvt["is"][item6])**-1))) <= 160

# EV2
for item in d_jk :
    for item2 in konsumen_keys :
        for item3 in Cvt_keys_jk :
            problem += 50 * (lp.lpSum(d["jk"][item] * Qdjk[item2] * (Cvt["jk"][item3])**-1)) <= 60
        
# EV3
for item in d_li :
    for item2 in manuf_keys :
        for item3 in Cvt_keys_li :
            for item4 in d_sl :
                for item5 in collector_keys :
                    for item6 in Cvt_keys_sl:
                        problem += 50 * (lp.lpSum(d["li"][item] * Qrli[item2] * (Cvt["li"][item3])**-1) + d["sl"][item4] * Qwsl[item5] * (Cvt["sl"][item6])**-1) <= 120

# EV4
for item in manuf_keys :
    for item2 in sekunder_keys :
        problem += 0.7 * (lp.lpSum(QPij[item] + Qmis[item2])) <= 150
        
# #Dummy QRli
# for item in manuf_keys:
#     problem += lp.lpSum(Qrli[item]) >= 100

# print("=================================")
print("Biaya Produksi : ", biaya_produksi)
# # print("Biaya Remanufaktur : ", biaya_remanufaktur)
# # print("Biaya Pengiriman I ke J : ", biaya_pengiriman_i_j)
# # print("Biaya Diskon : ", biaya_diskon)
# # print("Biaya Penanganan : ", biaya_penanganan)
# # print("Biaya Pengiriman J ke K : ", biaya_pengiriman_j_k)
# # print("Biaya Fixed Cost Collector : ", fixed_cost_collector)
# # print("Biaya Pemilahan: ", biaya_pemilahan)
# print("=================================")

problem.writeLP("Cost_Minimization")
problem.solve()
print("Status:", lp.LpStatus[problem.status])

status = problem.solve(lp.PULP_CBC_CMD(msg=0))
print(lp.LpStatus[status])

# print(problem)

for v in problem.variables():
    print(v.name, "=", v.varValue)

print("Total Biaya =", lp.value(problem.objective))