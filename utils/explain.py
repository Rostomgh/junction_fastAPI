def explain_prediction(sample_input, env_pred_label, bact_pred_label):
    reasons = []

    if env_pred_label in ['Poor', 'Moderate']:
        if sample_input['DissolvedOxygen (mg/L)'] < 5:
            reasons.append("🔴 Dissolved oxygen is below optimal level (< 5 mg/L).")
        if sample_input['pH'] < 6.5 or sample_input['pH'] > 8.5:
            reasons.append("⚠️ pH is outside the healthy range for fish (6.5–8.5).")
        if sample_input['SecchiDepth (m)'] < 1:
            reasons.append("⚠️ Water transparency is low, which can affect light penetration.")
        if env_pred_label == 'Moderate':
            reasons.append("⚠️ Environment quality is moderate; it's not critical but requires monitoring.")

    if bact_pred_label in ['High', 'Medium']:
        if sample_input['WaterTemp (C)'] > 28:
            reasons.append("🌡️ Warm water increases bacterial growth risk.")
        if sample_input['Salinity (ppt)'] < 3:
            reasons.append("🌊 Low salinity may support bacterial presence.")
        if sample_input['DissolvedOxygen (mg/L)'] < 5:
            reasons.append("⚠️ Low oxygen may lead to bacteria thriving in low-oxygen zones.")
        if bact_pred_label == 'Medium':
            reasons.append("⚠️ Bacteria level is medium; take preventive steps.")

    return reasons
