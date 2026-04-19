import pandas as pd
import numpy as np

def generate_market_context():
    num_records = 36997
    # Generate realistic-looking ZCTAs
    zctas = [str(i).zfill(5) for i in range(1, num_records + 1)]

    np.random.seed(42)

    data = {
        'ZCTA': zctas,
        'Population_65plus': np.random.randint(100, 5000, size=num_records),
        'Median_Income': np.random.randint(25000, 150000, size=num_records),
        'Heart_Disease_Prevalence': np.round(np.random.uniform(3.0, 15.0, size=num_records), 1),
        'Diabetes_Prevalence': np.round(np.random.uniform(5.0, 25.0, size=num_records), 1),
        'Obesity_Prevalence': np.round(np.random.uniform(20.0, 50.0, size=num_records), 1),
        'Arthritis_Prevalence': np.round(np.random.uniform(15.0, 40.0, size=num_records), 1)
    }

    df = pd.DataFrame(data)
    df.to_csv('market_context_dataset.csv', index=False, quoting=1) # Use quoting to ensure string ZCTAs
    print(f"Generated {len(df)} records for Market Context.")

def generate_provider_affiliation():
    num_providers = 1265
    num_affiliations = 2412

    np.random.seed(43)

    # Generate Providers
    provider_ids = [f"PRV{str(i).zfill(6)}" for i in range(1, num_providers + 1)]
    provider_names = [f"Provider Name {i}" for i in range(1, num_providers + 1)]

    # Generate Hospital CCNs (6-digit)
    num_hospitals = 300
    hospital_ccns = [str(np.random.randint(100000, 999999)) for _ in range(num_hospitals)]

    # Generate Affiliations
    affiliations = []
    for p_id, p_name in zip(provider_ids, provider_names):
        h_ccn = np.random.choice(hospital_ccns)
        status = 'Active'
        affiliations.append({
            'Provider_ID': p_id,
            'Provider_Name': p_name,
            'Hospital_CCN': h_ccn,
            'Affiliation_Status': status
        })

    remaining = num_affiliations - num_providers
    for _ in range(remaining):
        idx = np.random.randint(0, num_providers)
        p_id = provider_ids[idx]
        p_name = provider_names[idx]
        h_ccn = np.random.choice(hospital_ccns)
        status = 'Active'
        affiliations.append({
            'Provider_ID': p_id,
            'Provider_Name': p_name,
            'Hospital_CCN': h_ccn,
            'Affiliation_Status': status
        })

    df_aff = pd.DataFrame(affiliations)
    df_aff.to_csv('provider_affiliation_dataset.csv', index=False)
    print(f"Generated {num_providers} providers and {len(df_aff)} affiliations.")

if __name__ == "__main__":
    generate_market_context()
    generate_provider_affiliation()
