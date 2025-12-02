from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd

# Load Excel
df = pd.read_excel("realestate.xlsx")

@api_view(['POST'])
def analyze_area(request):
    query = request.data.get("query", "").strip()
    area = query.split()[-1].strip()

    # Debug output
    print("=== DEBUG ===")
    print("User Query:", query)
    print("Extracted Area:", area)
    print("Excel Areas:", df["final location"].unique())
    print("================")

    # Filtering
    mask = df["final location"].str.lower().str.contains(area.lower(), na=False)
    data = df[mask]

    if data.empty:
        return Response({"error": "No data found for this area"}, status=404)

    summary = f"{area} has shown stable real-estate activity."

    chart = {
        "years": data["year"].tolist(),
        "price": data["flat_sold - igr"].tolist(),
        "demand": data["total sold - igr"].tolist()
    }

    return Response({
        "summary": summary,
        "chart": chart,
        "table": data.to_dict(orient="records")
    })
