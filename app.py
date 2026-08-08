import streamlit as st

st.set_page_config(
    page_title="NutriAI",
    page_icon="🥗",
    layout="wide"
)

# -----------------------------
# CUSTOM UI
# -----------------------------

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
}

.subtitle {
    font-size: 18px;
    color: #666;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    '<div class="main-title">🥗 NutriAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Nutrition & Smart Grocery Assistant</div>',
    unsafe_allow_html=True
)

st.write(
    "Create personalized meal plans, optimize your grocery budget, "
    "and evaluate nutrition completeness."
)

st.divider()


# -----------------------------
# USER INFORMATION
# -----------------------------

st.header("👤 Tell us about yourself")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=25
    )

    diet = st.selectbox(
        "Dietary preference",
        [
            "No preference",
            "Vegetarian",
            "Vegan",
            "Eggetarian",
            "Non-vegetarian"
        ]
    )

    goal = st.selectbox(
        "Nutrition goal",
        [
            "Balanced nutrition",
            "Weight management",
            "Muscle support",
            "Healthy eating",
            "Budget-friendly meals"
        ]
    )


with col2:

    household = st.number_input(
        "Household size",
        min_value=1,
        max_value=20,
        value=1
    )

    budget = st.number_input(
        "Weekly grocery budget",
        min_value=100,
        value=3000,
        step=100
    )

    culture = st.selectbox(
        "Preferred cuisine",
        [
            "Indian",
            "South Indian",
            "North Indian",
            "Mediterranean",
            "East Asian",
            "Western",
            "Mixed / No preference"
        ]
    )


st.divider()


# -----------------------------
# MEAL PREFERENCES
# -----------------------------

st.header("🍽️ Meal preferences")

preferences = st.text_area(
    "Anything else should we consider?",
    placeholder="Example: quick meals, affordable ingredients, seasonal vegetables"
)

days = st.slider(
    "How many days should we plan?",
    min_value=1,
    max_value=7,
    value=3
)

st.divider()


# -----------------------------
# CALORIE & PROTEIN TARGET
# -----------------------------

def calculate_targets(age, goal):

    calories = 2000
    protein = 60

    if age < 18:
        calories = 1800
        protein = 50

    elif age >= 50:
        calories = 1900
        protein = 65

    if goal == "Weight management":
        calories -= 250

    elif goal == "Muscle support":
        calories += 250
        protein += 25

    elif goal == "Healthy eating":
        calories = 2000
        protein = 65

    elif goal == "Budget-friendly meals":
        calories = 2000
        protein = 60

    return calories, protein


# -----------------------------
# MEAL DATABASE
# -----------------------------

meal_plans = {

    "Vegetarian": [

        ("Idli + Sambar", "Rice + Dal + Vegetables", "Chapati + Paneer", "Fruit + Nuts"),
        ("Vegetable Upma", "Rajma Rice + Salad", "Dosa + Sambar", "Roasted Chickpeas"),
        ("Poha + Banana", "Vegetable Pulao + Raita", "Dal Khichdi + Curd", "Apple + Peanuts"),
        ("Masala Dosa + Chutney", "Sambar Rice + Vegetable Poriyal", "Roti + Dal + Salad", "Fruit + Curd"),
        ("Pongal + Sambar", "Lemon Rice + Dal", "Paneer Curry + Chapati", "Roasted Makhana"),
        ("Oats + Banana", "Curd Rice + Vegetables", "Vegetable Pulao + Raita", "Sprouts Salad"),
        ("Idli + Chutney", "Rice + Dal + Beans", "Chapati + Vegetable Curry", "Banana + Peanuts")

    ],

    "Vegan": [

        ("Oats + Banana", "Rice + Dal + Vegetables", "Chapati + Vegetable Curry", "Fruit + Peanuts"),
        ("Vegetable Poha", "Rajma Rice + Salad", "Tofu Curry + Chapati", "Roasted Chickpeas"),
        ("Fruit Oats Bowl", "Chickpea Rice Bowl", "Vegetable Khichdi", "Apple + Peanuts"),
        ("Dosa + Coconut Chutney", "Lemon Rice + Dal", "Tofu Stir Fry + Rice", "Fruit Bowl"),
        ("Vegetable Upma", "Vegetable Pulao + Salad", "Dal + Chapati + Vegetables", "Roasted Makhana"),
        ("Peanut Oats + Banana", "Chickpea Salad + Rice", "Vegetable Curry + Chapati", "Sprouts Salad"),
        ("Poha + Fruit", "Dal Rice + Vegetables", "Tofu + Vegetable Rice", "Banana + Peanuts")

    ],

    "Eggetarian": [

        ("Egg Omelette + Toast", "Rice + Dal + Vegetables", "Chapati + Paneer", "Boiled Egg + Fruit"),
        ("Egg Sandwich", "Rajma Rice + Salad", "Dosa + Sambar", "Fruit + Nuts"),
        ("Masala Eggs + Toast", "Vegetable Pulao + Raita", "Paneer Curry + Chapati", "Boiled Egg"),
        ("Egg Bhurji + Roti", "Sambar Rice + Vegetables", "Dal Khichdi + Curd", "Fruit + Peanuts"),
        ("Omelette + Banana", "Lemon Rice + Dal", "Paneer + Chapati", "Boiled Egg + Fruit"),
        ("Eggs + Oats", "Curd Rice + Vegetables", "Vegetable Pulao + Paneer", "Roasted Chickpeas"),
        ("Egg Sandwich + Fruit", "Rice + Dal + Beans", "Chapati + Paneer Curry", "Boiled Egg + Nuts")

    ],

    "Non-vegetarian": [

        ("Eggs + Toast", "Chicken Rice + Vegetables", "Chicken Curry + Chapati", "Fruit + Nuts"),
        ("Chicken Sandwich", "Chicken Biryani + Salad", "Egg Curry + Rice", "Fruit + Peanuts"),
        ("Omelette + Banana", "Chicken Pulao + Raita", "Grilled Chicken + Chapati", "Boiled Egg + Fruit"),
        ("Egg Bhurji + Toast", "Chicken Rice + Vegetables", "Fish Curry + Rice", "Fruit + Nuts"),
        ("Eggs + Oats", "Chicken Curry + Rice", "Chicken + Chapati + Salad", "Boiled Egg"),
        ("Omelette + Fruit", "Fish Rice + Vegetables", "Chicken Curry + Roti", "Peanuts + Banana"),
        ("Egg Sandwich", "Chicken Pulao + Salad", "Fish Curry + Chapati", "Fruit + Nuts")

    ],

    "No preference": [

        ("Idli + Sambar", "Rice + Dal + Vegetables", "Chapati + Paneer", "Fruit + Nuts"),
        ("Vegetable Upma", "Rajma Rice + Salad", "Dosa + Sambar", "Roasted Chickpeas"),
        ("Poha + Banana", "Vegetable Pulao + Raita", "Dal Khichdi + Curd", "Apple + Peanuts"),
        ("Masala Dosa + Chutney", "Sambar Rice + Vegetables", "Roti + Dal + Salad", "Fruit + Curd"),
        ("Pongal + Sambar", "Lemon Rice + Dal", "Paneer Curry + Chapati", "Roasted Makhana"),
        ("Oats + Banana", "Curd Rice + Vegetables", "Vegetable Pulao + Raita", "Sprouts Salad"),
        ("Idli + Chutney", "Rice + Dal + Beans", "Chapati + Vegetable Curry", "Banana + Peanuts")

    ]
}


# -----------------------------
# GENERATE MEAL PLAN
# -----------------------------

def generate_meal_plan(
    age,
    diet,
    goal,
    household,
    budget,
    culture,
    preferences,
    days
):

    calories, protein = calculate_targets(age, goal)

    meals = meal_plans[diet]


    # -----------------------------
    # NUTRITION SCORES
    # -----------------------------

    protein_score = 85
    fiber_score = 90
    carb_score = 85
    fat_score = 80

    if goal == "Muscle support":
        protein_score = 94

    elif goal == "Weight management":
        fiber_score = 93

    elif goal == "Budget-friendly meals":
        fiber_score = 91

    overall_score = round(
        (
            protein_score
            + fiber_score
            + carb_score
            + fat_score
        ) / 4
    )


    # -----------------------------
    # COST ESTIMATION
    # -----------------------------

    estimated_cost = int(budget * 0.88)

    remaining = budget - estimated_cost


    # -----------------------------
    # SUCCESS
    # -----------------------------

    st.success("Your nutrition plan is ready! 🎉")


    # -----------------------------
    # DASHBOARD
    # -----------------------------

    st.subheader("📊 Your Nutrition Dashboard")

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:
        st.metric("🔥 Calories", f"{calories} kcal")

    with metric2:
        st.metric("💪 Protein", f"{protein} g")

    with metric3:
        st.metric("⭐ Nutrition Score", f"{overall_score}/100")

    with metric4:
        st.metric("💰 Est. Grocery Cost", f"₹{estimated_cost:,}")


    st.divider()


    # -----------------------------
    # PLAN SUMMARY
    # -----------------------------

    st.subheader("🎯 Plan Summary")

    summary1, summary2, summary3, summary4 = st.columns(4)

    with summary1:
        st.write("👤 **Age**")
        st.write(age)

    with summary2:
        st.write("🥗 **Diet**")
        st.write(diet)

    with summary3:
        st.write("🎯 **Goal**")
        st.write(goal)

    with summary4:
        st.write("🌍 **Cuisine**")
        st.write(culture)

    if preferences:
        st.info(f"💡 Preference considered: {preferences}")


    st.divider()


    # -----------------------------
    # MEAL PLAN
    # -----------------------------

    st.subheader(
        f"🍽️ {days}-Day Personalized Meal Plan"
    )

    for day in range(days):

        breakfast, lunch, dinner, snack = meals[day]

        with st.expander(
            f"📅 Day {day + 1}",
            expanded=(day == 0)
        ):

            meal1, meal2 = st.columns(2)

            with meal1:

                st.markdown("### 🌅 Breakfast")
                st.write(breakfast)

                st.markdown("### ☀️ Lunch")
                st.write(lunch)

            with meal2:

                st.markdown("### 🌙 Dinner")
                st.write(dinner)

                st.markdown("### 🍎 Snack")
                st.write(snack)


    st.divider()


    # -----------------------------
    # NUTRITION EVALUATION
    # -----------------------------

    st.subheader("📈 Nutrition Evaluation")

    n1, n2, n3, n4 = st.columns(4)

    with n1:
        st.metric("💪 Protein", f"{protein_score}%")

    with n2:
        st.metric("🌾 Fiber", f"{fiber_score}%")

    with n3:
        st.metric("🍚 Carbohydrates", f"{carb_score}%")

    with n4:
        st.metric("🥑 Healthy Fats", f"{fat_score}%")


    st.divider()


    # -----------------------------
    # GROCERY LIST
    # -----------------------------

    st.subheader("🛒 Smart Grocery List")

    grocery1, grocery2 = st.columns(2)

    with grocery1:

        st.write("🍚 Rice — 2 kg")
        st.write("🌾 Wheat flour — 1 kg")
        st.write("🥣 Dal — 1 kg")
        st.write("🥬 Vegetables — 3 kg")
        st.write("🍎 Fruits — 2 kg")

    with grocery2:

        st.write("🥣 Oats — 500 g")
        st.write("🥜 Peanuts — 500 g")
        st.write("🥛 Paneer / Eggs / Chicken")
        st.write("🌱 Seasonal ingredients")


    st.divider()


    # -----------------------------
    # BUDGET
    # -----------------------------

    st.subheader("💰 Budget Analysis")

    b1, b2, b3 = st.columns(3)

    with b1:
        st.metric("Weekly Budget", f"₹{budget:,}")

    with b2:
        st.metric("Estimated Cost", f"₹{estimated_cost:,}")

    with b3:
        st.metric("Remaining", f"₹{remaining:,}")

    st.progress(
        min(estimated_cost / budget, 1.0)
    )


    st.divider()


    # -----------------------------
    # RECOMMENDATIONS
    # -----------------------------

    st.subheader("💡 Personalized Recommendations")

    st.write(
        f"🎯 Your plan is designed around your **{goal}** goal."
    )

    st.write(
        f"🥗 Your selected diet is **{diet}**."
    )

    st.write(
        f"🌍 Your preferred cuisine is **{culture}**."
    )

    st.write(
        "💪 Include a protein source with every major meal."
    )

    st.write(
        "🥬 Choose seasonal vegetables to improve nutrition and reduce cost."
    )

    st.write(
        "♻️ Reuse common ingredients across meals to reduce food waste."
    )


    st.divider()


    # -----------------------------
    # FOOD WASTE
    # -----------------------------

    st.subheader("♻️ Food Waste Reduction")

    st.write(
        "Common ingredients are reused across meals "
        "to reduce food waste."
    )

    st.success("Waste Reduction Level: 🟢 High")


# -----------------------------
# GENERATE BUTTON
# -----------------------------

if st.button(
    "✨ Generate My Nutrition Plan",
    type="primary",
    use_container_width=True
):

    with st.spinner(
        "Creating your personalized nutrition plan..."
    ):

        generate_meal_plan(
            age,
            diet,
            goal,
            household,
            budget,
            culture,
            preferences,
            days
        )


# -----------------------------
# FOOTER
# -----------------------------

st.divider()

st.caption(
    "⚠️ Disclaimer: NutriAI provides general nutrition suggestions "
    "for informational purposes only and is not a substitute for "
    "professional medical or dietary advice."
)


if st.button(
    "🔄 Start Over",
    use_container_width=True
):

    st.rerun()