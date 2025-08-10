def analyze_family_photo(image_path):
    faces = detect_faces(image_path)
    results = []

    for face in faces:
        age = estimate_age(face)
        gender = estimate_gender(face)
        position = get_position(face)

        # Heuristic rules for role assignment
        if age > 60:
            role = "Grandparent"
        elif age > 30 and gender == "male":
            role = "Father"
        elif age > 30 and gender == "female":
            role = "Mother"
        elif age < 18:
            role = "Child"
        else:
            role = "Uncertain"

        results.append({
            "location": position,
            "estimated_age": age,
            "gender": gender,
            "role": role
        })

    return results
