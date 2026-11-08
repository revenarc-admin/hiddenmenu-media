"""Days 1-30, Kitchen Ticket style, rewritten in a plain human voice.
Each day: folder, slides, caption, source line (or None), hashtags.
Facts are the same verified ones used in v2."""

P = {}
C = {}  # captions: (text, source, tags)

def note(label, lead, body=None, src=None): return dict(t="note", label=label, lead=lead, body=body, src=src)
def big(label, num, lead, body=None, src=None, numsize=190): return dict(t="big", label=label, num=num, lead=lead, body=body, src=src, numsize=numsize)
def rows(label, title, r): return dict(t="rows", label=label, title=title, rows=r)
def vs(label, a, b, title=None): return dict(t="vs", label=label, a=a, b=b, title=title)
def tip(title, body, box=None, label="What to do with this"): return dict(t="tip", label=label, title=title, body=body, box=box)
def end(title, body=None, label="Last thing"): return dict(t="end", label=label, title=title, body=body)
def cover(head, punch=None, voids=None, stamp=None): return dict(t="cover", head=head, punch=punch, voids=voids, stamp=stamp)

# ---------------------------------------------------------------- 1
P[1] = ("01_no_dollar_signs", [
    cover("Fancy menus leave off the dollar sign.", "Somebody tested whether it works.", ["dollar sign"], "86'D"),
    note("The test", "Cornell, 2009. One restaurant, 201 lunch guests, three versions of the same menu.",
         "One said $20.00. One said 20. One spelled it out: twenty dollars."),
    big("What happened", "+8%", "more spent by the people with no dollar sign.",
        "About $5.55 a head. Writing out \"dollars\" did no better than the $ symbol.",
        "Yang, Kimes & Sessarego, Cornell, 2009"),
    note("Why, probably", "The researchers think any reminder of money makes you think about cost.",
         "Take the reminder away and you think about lunch instead."),
    note("To be fair", "It's a small nudge.",
         "How many people were at the table and how long they stayed mattered way more. But it costs nothing, so lots of places do it."),
    tip("A bare 32 is still $32.", "Read it with the sign in your head and order what you actually want.", "32 = $32"),
    end("That's the trick.", "There are nine more like it."),
])
C[1] = ("""Fancy restaurants leave the dollar sign off the menu. In 2009 a Cornell team checked whether that changes anything.

201 lunch guests got one of three menus: $20.00, 20, or "twenty dollars." The people with the plain number spent about 8% more, roughly $5.55 a head.

It's a small effect. Party size mattered more. But it's free for the restaurant, so you see it everywhere.""",
"Yang, Kimes & Sessarego, Cornell Center for Hospitality Research, 2009",
"#menupsychology #restaurants #foodie #diningout #restaurantlife #hospitality #foodfacts")

# ---------------------------------------------------------------- 2
P[2] = ("02_check_in", [
    cover("Hotel check-in is one person, a line, and a phone that won't stop.", "Some guests make it easier.", None, None),
    note("Picture it", "One agent. A tour bus just pulled up. Someone on hold about parking.",
         "They remember who was easy to deal with. Everyone does."),
    rows("What helps", "Three things, all free", [
        ("Be nice when they're slammed", "\"No rush\" is rare enough that people notice."),
        ("Ask, don't demand", "\"Anything nicer open tonight?\" leaves room for a yes."),
        ("Show up later in the day", "By evening they know which rooms are still empty."),
    ]),
    vs("Same request, two ways", ("Gets a no", "\"Upgrade me.\"", "Now they have to defend the rules.", False),
       ("Gets a maybe", "\"Anything nicer?\"", "Now they get to be the one who helped.", True)),
    note("To be fair", "If the hotel is full, there's nothing to give.", "None of this is a guarantee. It just costs you nothing to try."),
    tip("Ask a question.", "Works at hotels, restaurants and airline counters. Pretty much anywhere a person can say yes."),
    end("One more for the road.", "The cheat sheet is restaurants, but the spirit is the same."),
])
C[2] = ("""The front desk is usually one or two people, a line, and a phone that keeps ringing. They remember who made that easier.

Three free things that help: be patient when they're slammed, ask instead of demand ("anything nicer open tonight?" beats "upgrade me"), and check in later in the day when they know what's still empty.

No guarantees. A full hotel has nothing to give. But it costs nothing to ask nicely.""",
None,
"#travel #hoteltips #traveltips #hotels #hospitality #frontdesk #travelsmart")

# ---------------------------------------------------------------- 3
P[3] = ("03_wine_glass", [
    cover("The restaurant buys a bottle. You buy one glass.", "Guess how many glasses pay for the bottle.", None, None),
    note("Think about it", "A bottle pours about five glasses.", "So how many does the restaurant need to sell before the bottle is paid off?"),
    big("Often", "1", "glass.", "A common rule in the business: price one glass at about what the whole bottle cost them.",
        "VinePair, The Cost of That Bottle of Wine, Explained"),
    note("Why", "An open bottle doesn't keep.", "If you're the only one who orders that wine tonight, the rest might go down the sink. Your glass covers that risk."),
    vs("Quick math", ("By the glass", "5 x $14", "$70 for one bottle's worth.", False),
       ("The bottle", "$52", "Better if you're each having two.", True)),
    tip("Divide bottle by glass.", "If the answer is under 3, get the bottle. If you all want different wines, glasses still make sense.", "$52 / $14 = 3.7"),
    end("Wine's done.", "The cheat sheet has the rest of the menu."),
])
C[3] = ("""One glass of wine is often priced at about what the restaurant paid for the whole bottle.

It sounds greedy, but there's a reason. An open bottle doesn't keep, and if nobody else orders that wine tonight, the rest gets poured out.

Quick check before you order: bottle price divided by glass price. Under 3 and you both want two glasses? Get the bottle.

Glass or bottle person? Tell me below.""",
"VinePair, vinepair.com/wine-blog/the-cost-of-that-bottle-of-wine-explained",
"#winetips #winelover #wine #restaurants #sommelier #winelist #foodie")

# ---------------------------------------------------------------- 4
P[4] = ("02_golden_triangle_myth", [
    cover("Menu consultants swore you look top-right first.", "Then somebody checked.", ["golden triangle", "sweet spot", "top-right rule"], "86'D"),
    note("The story", "Your eyes supposedly zigzag to the top-right corner of a menu.", "So for years restaurants were told to put the expensive stuff there."),
    note("The problem", "Nobody had actually watched anyone read a menu.", "It got repeated for decades because it sounded like science."),
    note("What the eye tracker saw", "2012. A researcher named Sybil Yang put eye trackers on real diners.",
         "They read the menu like a book. Top to bottom. The way you're reading this.",
         "Yang, Int'l Journal of Hospitality Management, 2012"),
    note("What does matter", "First and last.", "People notice the first dish in a section and remember the last one. That's where restaurants put what they want to sell."),
    tip("So read the middle.", "The middle of each section is where nobody is pushing anything at you. That's often where the value is.", "First >> middle << last"),
    end("That one was a myth.", "The cheat sheet is the ten that aren't."),
])
C[4] = ("""For years, menu consultants said your eyes go to the top-right corner first, so that's where the expensive dishes should go.

Nobody checked until 2012. Sybil Yang put eye trackers on real diners. They read the menu like a book, top to bottom, in order.

What does get attention: the first and last dish in each section. So read the middle.""",
"Yang, International Journal of Hospitality Management, 2012",
"#menupsychology #restaurants #mythbusting #foodie #restaurantlife #hospitality #foodfacts")

# ---------------------------------------------------------------- 5
P[5] = ("05_four_minutes", [
    cover("Your server vanished for four minutes.", "Here's a guess at where they went.", None, None),
    big("Minute 1", "6", "tables at once.", "Two waiting on drinks. One ready to order. One wants the check. Two just sat down."),
    note("Minute 2", "The kitchen, about your allergy.", "Checking with the chef that the sauce really has no nuts in it."),
    note("Minute 3", "A steak goes back. A lemonade goes over.", "One plate came out wrong. A kid on table 12 knocked a drink into a lap."),
    note("Minute 4", "Back at your table.", "\"Sorry about that. What can I get you?\""),
    note("To be fair", "Sometimes service is just slow.", "Say something early and kindly. Most servers would much rather fix it than have you sit there annoyed."),
    end("Patience counts.", "So does a decent tip."),
])
C[5] = ("""When your server disappears for a few minutes on a Friday, they're usually not on their phone.

Six tables at once. A trip to the kitchen to double check someone's allergy. A steak that came out wrong. A drink knocked over two tables down. Then back to you, smiling.

Sometimes service really is slow. If it is, say so early and nicely. It almost always gets fixed faster than you'd think.""",
None,
"#restaurantlife #serverlife #hospitality #restaurants #diningout #foodie #behindthescenes")

# ---------------------------------------------------------------- 6
P[6] = ("06_book_direct", [
    cover("Book with the hotel or on a booking site?", "Depends what you want.", None, None),
    note("Follow the money", "Booking sites charge the hotel a commission.", "When you book direct, the hotel keeps more. That's why some of them throw in perks."),
    vs("Who's good at what", ("Book direct", "Perks", "Points, room requests, easier changes.", True),
       ("Booking site", "Choice", "Everything side by side. Bundles.", False)),
    tip("Find the price, then call.", "Look up the best rate online, then ask the hotel if they'll match it or add breakfast or parking. Worst case they say no.", "Search wide >> book direct"),
    note("To be fair", "Not every hotel will match.", "And some cheap rates come with strict no-cancel rules. Read those before you click."),
    note("Always", "Compare the final total.", "Taxes and fees in. The nightly rate on its own tells you very little."),
    end("Booked.", "The cheat sheet is for when you get there and sit down to eat."),
])
C[6] = ("""Booking sites charge hotels a commission on every stay. Book direct and the hotel keeps more, which is why some of them offer points, perks or easier changes.

Booking sites are better for comparing. So use both: find the best price online, then call the hotel and ask if they'll match it or throw in breakfast or parking.

Not every hotel will. Compare the full total, fees included, either way.""",
None,
"#travel #hoteltips #traveltips #hotels #booking #travelsmart #vacation")

# ---------------------------------------------------------------- 7
P[7] = ("07_tablet_tip", [
    cover("The tablet spins around.", "20%. 25%. 30%. Of what, exactly?", None, None),
    note("Look closer", "Those buttons are a percentage of something.", "On some screens, that something is the total after tax."),
    note("Which means", "Every button is a little bigger than you think.", "You're tipping on the tax too."),
    big("Emily Post says", "15-20%", "of the pre-tax bill for sit-down service.", "And tipping on the pre-tax amount is normal.",
        "Emily Post Institute, tipping guide", numsize=150),
    note("At the counter", "No table service, no obligation.", "Emily Post calls it optional. Extra is kind. It's not owed."),
    tip("Look at the dollar amount.", "Not the percent. If it looks off, hit custom and type in what you meant.", "Custom is a button too"),
    end("That's the tablet.", "The menu has a few tricks of its own."),
])
C[7] = ("""Next time the tablet spins around, check what the percentages are based on. Some screens use the total after tax, so every option is a bit bigger than it looks.

The Emily Post Institute says 15 to 20% of the pre-tax bill is right for sit-down service. At a counter with no table service, a tip is optional.

Look at the dollar amount, not the percent. Custom is always an option.""",
"Emily Post Institute, emilypost.com/advice/general-tipping-guide and emilypost.com/advice/finer-points-of-tipping",
"#tipping #restaurants #diningout #etiquette #foodie #moneytips #hospitality")

# ---------------------------------------------------------------- 8
P[8] = ("08_decoy_steak", [
    cover("Nobody's supposed to order the $95 steak.", "It has another job.", None, None),
    rows("Read this section", "The steaks", [("Tomahawk  95", "Big, loud, at the top."), ("Ribeye  48", "Suddenly sounds sensible."), ("Filet  36", "Now it feels like the cheap one.")]),
    note("This is called anchoring", "The first price you see sets the scale.", "Everything after it gets judged against that number. Next to $95, $48 feels fine."),
    vs("Same ribeye", ("On its own", "$48", "Feels expensive.", False), ("Under a $95", "$48", "Feels reasonable.", True)),
    note("To be fair", "Some people do order it.", "And the restaurant is happy when they do. But mostly it's there to make the rest look fair."),
    tip("Cover the top one with your thumb.", "Would you still pay $48 for the ribeye? Decide from there.", "Thumb over the $95"),
    end("Steak's done.", "Nine more on the cheat sheet."),
])
C[8] = ("""The $95 tomahawk at the top of the steak section isn't really there to be ordered. It's there so the $48 ribeye under it looks reasonable.

It's called anchoring. The first number sets the scale for everything you read after it.

Some people do order it, and the restaurant is glad. But try covering it with your thumb and asking if you'd still pay $48.""",
None,
"#menupsychology #steakhouse #restaurants #foodie #steak #diningout #foodfacts")

# ---------------------------------------------------------------- 9
P[9] = ("09_second_cheapest", [
    cover("\"Never order the second-cheapest wine.\"", "Two economists checked 6,335 bottles.", ["second-cheapest rip-off"], "86'D"),
    note("The story", "Restaurants know you won't order the cheapest bottle.", "So, supposedly, they hide the biggest markup one step up."),
    big("The test", "6,335", "wines on London restaurant lists.", "Checked against shop prices by economists at LSE and the University of Sussex.",
        "de Meza & Pathania, LSE Research Online", numsize=160),
    note("What they found", "The second-cheapest had a lower markup than the next four bottles up.", "Markups climbed from the bottom and peaked somewhere in the middle."),
    note("So if anything", "Watch the middle of the list.", "That's where the percentages were highest in their data."),
    tip("Ask what they like under $50.", "Staff favorites are often the best value on the list. And nobody minds the question."),
    end("Wine list, sorted.", "The rest of the menu is on the cheat sheet."),
])
C[9] = (""""Never order the second-cheapest wine, that's where they hide the markup." Two economists checked.

They looked at 6,335 wines on London restaurant lists and compared them to shop prices. The second-cheapest bottle had a lower markup than the next four above it. The highest percentages were in the middle of the list.

Easiest move: ask what they like under $50.""",
"de Meza and Pathania, LSE Research Online, researchonline.lse.ac.uk/id/eprint/110874",
"#wine #winetips #winelover #restaurants #mythbusting #sommelier #foodie")

# ---------------------------------------------------------------- 10
P[10] = ("10_late_checkout", [
    cover("Late checkout is mostly about when you ask.", "And how.", None, None),
    vs("Timing", ("Usually no", "11:55am", "The day's rooms are already planned.", False),
       ("Often yes", "The night before", "Housekeeping can work around you.", True)),
    rows("How to ask", "Three small things", [("Make it a question", "\"Is a late checkout possible?\""), ("Name a time", "\"Could we do 1pm?\" is easier to say yes to than \"as late as you can.\""), ("Mention your status", "A lot of loyalty programs include it.")]),
    note("When it's hard", "Sold-out nights.", "If tonight is full, they need your room. Weekday checkouts tend to be easier."),
    note("To be fair", "Some hotels charge for it.", "If they quote a fee, ask if there's a shorter free grace period."),
    tip("Ask the day before. Name a time.", "That's it. Two small changes.", "1pm, please"),
    end("Enjoy the sleep-in.", "Then go get lunch."),
])
C[10] = ("""Asking for late checkout at 11:55am usually gets a no. By then the day's rooms are already planned.

Ask the night before, make it a question, and name a time. "Could we do 1pm?" is easy to say yes to. "As late as possible" isn't.

Sold-out nights are harder, and some hotels charge for it. If they quote a fee, ask about a short free grace period.""",
None,
"#travel #hoteltips #traveltips #hotels #latecheckout #vacation #travelsmart")

# ---------------------------------------------------------------- 11
P[11] = ("11_where_tip_goes", [
    cover("You tipped your server.", "It probably didn't all stay with them.", None, None),
    note("Shared", "Tips are often pooled.", "Or servers \"tip out\" bussers, bartenders and food runners at the end of the night."),
    note("The law", "Managers can't take a cut.", "Under federal law, employers, managers and supervisors can't keep any part of employees' tips. Tip pool included.",
         "US Department of Labor, FLSA tips"),
    note("The kitchen", "Cooks can be in the pool, sometimes.", "If everyone is paid at least full minimum wage, cooks and dishwashers can share."),
    note("And the 18% on big tables", "Legally that's a service charge, not a tip.", "The IRS treats required charges that way. The restaurant decides how it's split.", "IRS Topic 761"),
    tip("If it matters to you, ask.", "It's fine to ask how a service charge is shared. Rules vary by state."),
    end("Tipped and done.", None),
])
C[11] = ("""Your tip often gets shared. A lot of restaurants pool tips or have servers tip out bussers, bartenders and runners.

Managers can't take any of it. That's federal law. Cooks and dishwashers can be included if everyone earns at least full minimum wage.

That automatic 18% on big tables? The IRS counts it as a service charge, not a tip, and the restaurant decides where it goes. If you want to know, ask.""",
"US Department of Labor, dol.gov/agencies/whd/flsa/tips ; IRS, irs.gov/taxtopics/tc761 . State rules vary.",
"#tipping #restaurants #serverlife #restaurantlife #hospitality #diningout #foodfacts")

# ---------------------------------------------------------------- 12
P[12] = ("12_menu_words", [
    cover("\"Hand-pulled.\" \"Grandma's recipe.\" \"Wood-fired.\"", "Those words are doing a job.", None, None),
    vs("Same sandwich", ("Plain", "Chicken sandwich", "Sounds like $14.", False), ("Menu voice", "Hot honey chicken", "Sounds like $20.", True)),
    note("Why it works", "If you can picture it, it feels worth more.", "Where it's from, how it's cooked, who made it. Each detail makes it easier to see."),
    rows("The usual suspects", "Four kinds of words", [("Place", "Baja. Sonoma."), ("Method", "Wood-fired. Slow-braised."), ("Feeling", "Grandma's. Classic."), ("Texture", "Crispy. Velvety.")]),
    note("To be fair", "Sometimes it's true.", "Sometimes it's just good writing. Often both, on the same menu."),
    tip("Ask what house-made means.", "\"Which things do you make here?\" The answer says a lot about the kitchen."),
    end("Read past the adjectives.", None),
])
C[12] = ("""A chicken sandwich sounds like $14. Hot honey chicken on a brioche bun sounds like $20.

Menus lean on four kinds of words: places (Baja, Sonoma), methods (wood-fired, slow-braised), feelings (grandma's, classic) and textures (crispy, velvety). If you can picture it, it feels worth more.

Sometimes it's all true. Ask what's made in house. The answer tells you a lot.""",
None,
"#menupsychology #restaurants #foodie #foodwriting #diningout #restaurantlife #foodfacts")

# ---------------------------------------------------------------- 13
P[13] = ("13_markup_quiz", [
    cover("Soda, pasta, steak or coffee.", "Which one has the biggest markup?", None, None),
    rows("Pick one", "Lock it in", [("Soda", None), ("Pasta", None), ("Steak", None), ("Coffee", None)]),
    big("Answer", "~10x", "on a fountain soda.", "Around 25 to 40 cents with the cup. Sells for $3 or $4.",
        "The Takeout ; RestaurantCalcs", numsize=170),
    note("Close second", "Coffee.", "Pennies a cup to make, and often refilled for free anyway."),
    note("The surprise", "Steak has one of the lowest.", "Good beef costs a lot to buy, so it gets marked up far less than drinks."),
    note("Why it evens out", "The soda helps pay for the steak.", "Cheap drinks with big markups keep the expensive plates from costing even more."),
    end("How'd you do?", "Tell me in the comments."),
])
C[13] = ("""Soda, pasta, steak or coffee. Which has the biggest restaurant markup?

Fountain soda, by a lot. It can cost a restaurant 25 to 40 cents with the cup and sell for $3 or $4. Coffee is close behind.

Steak has one of the lowest. Good beef costs a lot to buy. The drinks help keep it from costing even more.

What did you guess?""",
"The Takeout, thetakeout.com/1757210/overpriced-menu-tems-avoid ; RestaurantCalcs, restaurantcalcs.com/calculators/fountain-cost",
"#restaurants #foodfacts #foodie #quiz #diningout #restaurantlife #menupsychology")

# ---------------------------------------------------------------- 14
P[14] = ("14_resort_fees", [
    cover("$199 a night.", "Then $238 at checkout.", ["surprise resort fee"], "86'D"),
    vs("How it used to go", ("Advertised", "$199", "Per night.", False), ("At checkout", "$238", "Plus a $39 resort fee.", True)),
    big("Since", "May 12", "2025: US hotels have to show the total price up front.", "The FTC rule covers hotels and booking sites, resort and amenity fees included.",
        "FTC, Rule on Unfair or Deceptive Fees", numsize=150),
    vs("What's in, what isn't", ("Has to be in", "Fees", "Resort, amenity, anything mandatory.", True), ("Can come later", "Taxes", "And optional add-ons you choose.", False)),
    tip("Compare totals.", "Not nightly rates. If a mandatory fee shows up at check-in that wasn't in your total, push back.", "Screenshot the total"),
    note("Small habit", "Screenshot the price when you book.", "Takes two seconds. Saves an argument later."),
    end("Trip's booked.", None),
])
C[14] = ("""$199 a night, then $238 at checkout. That used to be normal.

Since May 12, 2025, an FTC rule says US hotels and booking sites have to show the total price up front, mandatory resort and amenity fees included. Taxes and optional extras can still come later.

Screenshot the total when you book. If a required fee shows up at check-in that wasn't there, push back.""",
"FTC, ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions",
"#travel #hoteltips #traveltips #resortfees #hotels #consumerrights #travelsmart")

# ---------------------------------------------------------------- 15
P[15] = ("15_market_price", [
    cover("Lobster ........ MP", "What does that actually mean?", None, None),
    big("You've seen it", "MP", "next to the lobster.", "No number. Also oysters, crab, whole fish, and sometimes steak."),
    note("Why", "The restaurant's cost changes week to week.", "Season, weather, the catch. A printed price could be wrong by Friday."),
    note("The catch", "There's nothing to compare.", "No number on the page makes it easy to order first and find out later."),
    note("To be fair", "Usually it's not a trick.", "Most places just don't want to reprint the menu every week. The price can still surprise you."),
    tip("\"What's the market price today?\"", "Ask before you order. Servers get asked this all the time."),
    end("Now you'll ask.", None),
])
C[15] = (""""MP" next to the lobster just means market price. Seafood costs swing week to week, so a printed number could be wrong by Friday.

It's usually not a trick. Most places just don't want to reprint the menu. But with no number, it's easy to order first and get surprised later.

Ask what it is today. Servers get that question all the time.""",
None,
"#seafood #restaurants #lobster #foodie #diningout #menupsychology #foodfacts")

# ---------------------------------------------------------------- 16
P[16] = ("16_still_or_sparkling", [
    cover("\"Still or sparkling?\"", "Notice what's not one of the options.", None, None),
    vs("Your choices", ("Option 1", "Still", "Bottled.", False), ("Option 2", "Sparkling", "Also bottled.", False)),
    note("Missing", "Tap water.", "Most of us answer the question we're asked instead of coming up with a third choice."),
    note("The money", "Bottled water is an easy sale.", "Costs them little. Adds a few dollars per person to the check."),
    note("To be fair", "A lot of servers ask out of habit.", "And some people really do want sparkling."),
    tip("\"Tap is great, thanks.\"", "Completely normal thing to say. Nobody good will blink."),
    end("Water's on the house.", None),
])
C[16] = (""""Still or sparkling?" Both answers are bottled. Tap water just isn't one of the options, and most of us answer the question we're asked.

Bottled water costs a restaurant very little and adds a few dollars a person to the check. Plenty of servers ask out of habit, and some guests do want it.

"Tap is great, thanks" is a perfectly normal answer.""",
None,
"#restaurants #diningout #menupsychology #foodie #water #restaurantlife #moneytips")

# ---------------------------------------------------------------- 17
P[17] = ("17_servers_wish", [
    cover("Seven small things", "that make a server's night easier.", None, None),
    rows("Before you order", "1 to 3", [("Allergies first", "It changes how the kitchen makes your food."), ("Splitting the check? Say so early", "Seconds now, ten minutes later."), ("8 people, 8pm, Saturday", "That takes time. Plan for it.")]),
    rows("If something's off", "4 and 5", [("They don't run the kitchen", "But they can fix things."), ("Say it right away", "Much easier to fix now than after you've left.")]),
    rows("At the end", "6 and 7", [("Lingering is real", "An hour after paying, on a busy night, costs them a table."), ("So is a real thank-you", "It goes further than you'd think.")]),
    tip("Servers, what's number 8?", "Leave it in the comments. The good ones go in a follow-up post.", label="Over to you"),
    end("Allergies and split checks first.", "The two easiest wins of the night."),
])
C[17] = ("""Seven small things that make a server's night easier:

1. Mention allergies first.
2. Splitting the check? Say so at the start.
3. A party of 8 at 8pm on a Saturday takes time.
4. They don't run the kitchen, but they can fix things.
5. Say something right away if it's wrong.
6. Lingering an hour after paying on a busy night costs them a table.
7. A real thank-you goes a long way.

Servers, what's number 8?""",
None,
"#serverlife #restaurantlife #hospitality #restaurants #diningout #etiquette #foodie")

# ---------------------------------------------------------------- 18
P[18] = ("18_price_changed", [
    cover("The hotel price went up while you were looking.", "It's not your cookies.", None, None),
    note("How it works", "Hotel prices move all day.", "Most hotels use revenue management. Prices go up and down with demand."),
    rows("What moves it", "Three big ones", [("How full the hotel is", "As rooms sell, the rest often cost more."), ("Something happening nearby", "Concerts, conventions, big games."), ("Cancellations", "Those can push prices back down.")]),
    note("The myth", "\"They raised it because I looked twice.\"", "Prices follow demand. Clearing your cookies won't fix a sold-out weekend."),
    tip("Book refundable. Keep checking.", "If the price drops before your cancellation deadline, rebook at the lower rate and cancel the old one.", "A free price lock"),
    end("Stop refreshing.", "Book it and check back."),
])
C[18] = ("""Hotel prices change all day. Most hotels use revenue management, so prices follow demand: how full they are, what's happening in town, and cancellations.

It isn't because you looked twice. Clearing your cookies won't help on a sold-out weekend.

What does help: book a refundable rate, keep checking, and rebook if it drops before the cancellation deadline.""",
None,
"#travel #hoteltips #traveltips #hotels #booking #travelsmart #vacation")

# ---------------------------------------------------------------- 19
P[19] = ("19_bread_basket", [
    cover("Does the leftover bread go to the next table?", "The food code has an answer.", ["recycled bread basket"], "86'D"),
    note("The rumor", "Your leftover bread gets served to someone else.", "One of the most repeated restaurant rumors there is."),
    note("The rule", "The FDA Food Code says no.", "Food that's been served to one guest can't be served to another.", "FDA Food Code 2022, 3-306.14"),
    vs("The exceptions", ("Can't go back out", "Bread", "Once it's been on your table.", False), ("Can go back out", "Sealed stuff", "Packaged crackers, unopened ketchup.", True)),
    note("Who checks", "Your local health department.", "Most states build their rules on the FDA code, and inspectors look for this."),
    note("To be fair", "Rules aren't always followed.", "But reusing bread is a real violation, and good kitchens don't risk it."),
    end("Eat the bread.", None),
])
C[19] = ("""Do restaurants reuse the bread basket? Under the FDA Food Code, they're not allowed to. Food served to one guest can't be served to another.

Sealed stuff is the exception: packaged crackers, unopened ketchup bottles.

Most states base their rules on the FDA code, and inspectors check. Rules aren't always followed, but it's a real violation.""",
"FDA Food Code 2022, section 3-306.14, fda.gov/food/retail-food-protection/fda-food-code . States adopt the code with their own changes.",
"#restaurants #foodsafety #mythbusting #foodfacts #foodie #restaurantlife #diningout")

# ---------------------------------------------------------------- 20
P[20] = ("20_price_endings", [
    cover("19.99. 19.95. 19.", "Same price, three different moods.", None, None),
    rows("Three endings", "Read them out loud", [("19.99", "Feels like a deal."), ("19.95", "Feels friendly."), ("19", "Feels sure of itself.")]),
    note(".99", "Says bargain.", "The classic store ending. Value menus use it because it reads as savings."),
    note("Whole numbers", "Say we don't do coupons here.", "Fine dining drops the cents and the dollar sign. The less it looks like a price tag, the less you think about price."),
    vs("Same money", ("Diner", "19.99", "Sounds cheap.", False), ("Bistro", "20", "Sounds nice.", True)),
    tip("Round up in your head.", "19.95 is 20. That's the number you're paying.", "19.95 = 20"),
    end("Rounded.", None),
])
C[20] = ("""19.99 feels like a deal. 19.95 feels friendly. A plain 19 feels confident.

Value menus use .99 because it reads as savings. Fine dining drops the cents, and often the dollar sign too, because the less it looks like a price tag, the less you think about price.

19.95 is 20. Round up in your head.""",
None,
"#menupsychology #pricing #restaurants #foodie #diningout #moneytips #foodfacts")

# ---------------------------------------------------------------- 21
P[21] = ("21_hotel_tipping", [
    cover("Who do you tip at a hotel?", "And how much?", None, None),
    big("Housekeeping", "$2-5", "a day, every day.", "With a note that says it's for housekeeping. The person cleaning can change day to day.",
        "Emily Post Institute", numsize=160),
    rows("Bags and cars", "When you arrive", [("Bellhop: $2 for the first bag", "Then $1 for each extra, $2 to $3 for extra help."), ("Valet: $2 to $5", "When the car comes back."), ("Doorman: $1 to $4 for luggage", "$1 to $2 for hailing a cab.")]),
    note("Concierge", "Questions are free.", "$5 to $10 for a dinner booking or tickets. About $15 for something hard to get."),
    tip("Tip housekeeping daily.", "Not one lump at the end. That way it reaches whoever actually cleaned your room."),
    note("Small habit", "Keep a few small bills in your bag.", "You'll use them all trip."),
    end("Packed.", None),
])
C[21] = ("""Hotel tipping in the US, going by the Emily Post Institute:

Housekeeping: $2 to $5 a day, left daily with a note, since the person cleaning can change.
Bellhop: $2 for the first bag, $1 for each extra.
Valet: $2 to $5 when your car comes back.
Concierge: questions are free. $5 to $10 for a booking or tickets.

Keep small bills in your bag.""",
"Emily Post Institute, emilypost.com/advice/general-tipping-guide (US guidelines)",
"#travel #tipping #hoteltips #traveltips #etiquette #hotels #vacation")

# ---------------------------------------------------------------- 22
P[22] = ("22_booking_jargon", [
    cover("Run of house. BAR. Package rate.", "What hotel booking words actually mean.", None, None),
    note("Run of house", "You get whatever room is free.", "Usually the cheapest rate. No say in the view, the bed or the room type."),
    note("Best available rate", "The normal public price.", "Often called BAR. Usually flexible, and the starting point for most discounts."),
    vs("The big choice", ("Non-refundable", "Cheaper", "Paid up front. Usually locked.", False), ("Flexible", "Freedom", "Costs a bit more. Cancel for free.", True)),
    note("Package rate", "The room plus extras.", "Breakfast, parking, credits. Only worth it if you'd buy those anyway."),
    tip("Read the rate name.", "It tells you more than the price does."),
    end("Decoded.", None),
])
C[22] = ("""Hotel booking words, in plain English:

Run of house: you get whatever room is free. Cheapest, no choice.
Best available rate (BAR): the normal public price, usually flexible.
Non-refundable: cheaper, paid up front, locked in.
Package rate: room plus extras like breakfast or parking. Only worth it if you'd buy them anyway.

Read the rate name before you book.""",
None,
"#travel #hoteltips #traveltips #hotels #booking #travelsmart #vacation")

# ---------------------------------------------------------------- 23
P[23] = ("23_three_myths", [
    cover("Three restaurant \"facts\" that aren't.", "Each one checked.", ["sweet spot", "second-cheapest rip-off", "recycled bread"], "86'D"),
    note("Myth 1", "Menus have a top-right sweet spot.", "Eye trackers say people read menus top to bottom, like a book.", "Yang, 2012"),
    note("Myth 2", "The second-cheapest wine is the worst deal.", "In 6,335 wines, it had a lower markup than the next four up.", "de Meza & Pathania, LSE"),
    note("Myth 3", "Leftover bread gets served again.", "The FDA Food Code doesn't allow it.", "FDA Food Code 3-306.14"),
    note("The pattern", "Most menu tricks online were never tested.", "The ones that were, like the missing dollar sign, are smaller than people claim."),
    tip("Ask where the study is.", "Including here. Every post on this page lists a source."),
    end("Myths, 86'd.", None),
])
C[23] = ("""Three restaurant "facts" that don't hold up:

The top-right sweet spot on menus. Eye trackers say we read top to bottom.
The second-cheapest wine as a rip-off. In 6,335 wines, its markup was lower than the next four.
Recycled bread baskets. The FDA Food Code doesn't allow it.

Most menu tricks online were never tested. Ask where the study is, including here.""",
"Science Codex (Yang 2012) ; LSE Research Online (de Meza and Pathania) ; FDA Food Code 3-306.14",
"#mythbusting #restaurants #foodfacts #foodie #menupsychology #wine #diningout")

# ---------------------------------------------------------------- 24
P[24] = ("24_busiest_15", [
    cover("7:15 on a Saturday.", "The worst 15 minutes to walk into a restaurant.", None, None),
    big("Saturday", "7:15", "Every table turns over at once.", "Early diners paying, reservations arriving, the bar three deep.", numsize=170),
    rows("Meanwhile", "Inside", [("The kitchen", "Twenty tickets in ten minutes."), ("The host stand", "Tetris with tables and servers."), ("The bar", "Every drink order lands at the same time.")]),
    vs("Same dinner", ("Chaos", "7:15", "Longer waits. Rushed service.", False), ("Calm", "6:00 or 8:30", "Same food. More attention.", True)),
    tip("Book the shoulder.", "Same kitchen, same menu, much better night.", "6:00 or 8:30"),
    end("Reservation moved.", None),
])
C[24] = ("""Around 7:15 on a Saturday, almost every table in a restaurant turns over at once. Early diners pay, reservations walk in, the kitchen gets twenty tickets in ten minutes.

Book 6:00 or 8:30 instead. Same food, same menu, and the staff actually has time for you.""",
None,
"#restaurants #restaurantlife #diningout #foodie #reservations #hospitality #weekend")

# ---------------------------------------------------------------- 25
P[25] = ("25_specials", [
    cover("Tonight's specials are read out loud.", "Listen for the part that's missing.", None, None),
    note("Notice", "The price rarely comes up.", "The dish gets a lovely description. The number, not so much."),
    note("Why it matters", "There's nothing to compare it to.", "With no printed price next to the regular menu, it's hard to tell if it's a deal."),
    note("Often", "Specials cost more.", "Seasonal or premium ingredients, priced to match."),
    note("To be fair", "They're often the best thing that night.", "Fresh fish. Something the chef is trying. Worth ordering, just know the price first."),
    tip("\"How much is the special?\"", "Totally normal question. Ask it every time."),
    end("Ask, then order.", None),
])
C[25] = ("""When a server reads the specials, notice what usually gets left out: the price.

Specials often use seasonal or premium ingredients and cost more than the regular menu. With no printed number, there's nothing to compare.

They're often the best thing on offer that night. Just ask how much before you say yes. It's a normal question.""",
None,
"#restaurants #diningout #menupsychology #foodie #chefspecial #restaurantlife #moneytips")

# ---------------------------------------------------------------- 26
P[26] = ("26_when_to_book", [
    cover("\"Always book a hotel on Tuesday.\"", "There's no magic day.", ["the magic booking day"], "86'D"),
    note("The real rule", "Prices follow demand.", "Advice about one perfect day rarely holds up everywhere."),
    vs("City hotels", ("Business", "Weekdays", "Fill up with work trips.", False), ("Leisure", "Weekends", "Fill up with vacations.", False), title="If your dates move, check both."),
    note("Resorts and big events", "Book early when everyone wants the same dates.", "Holidays, concerts, big games. As rooms sell, the rest cost more."),
    tip("Book refundable. Check again.", "If it drops before the cancellation deadline, rebook and cancel the old one."),
    note("Worth it", "Flexible rates cost a little more.", "Usually worth it, especially for trips that might change."),
    end("Book it.", None),
])
C[26] = ("""There's no single best day to book a hotel. Prices follow demand.

City hotels often fill on weekdays with work travel and on weekends with vacations, so check both if your dates are flexible. For holidays and big events, book early.

Then book refundable and check back. If it drops before the deadline, rebook.""",
None,
"#travel #hoteltips #traveltips #hotels #booking #travelsmart #vacation")

# ---------------------------------------------------------------- 27
P[27] = ("27_better_table", [
    cover("How to get a better table", "without being difficult about it.", None, None),
    rows("Before you go", "Set it up early", [("Be specific in the notes", "\"A booth if you have one\" is easy to plan for."), ("Mention the occasion", "Birthdays and anniversaries often get the nicer tables.")]),
    vs("At the door", ("Hard for the host", "\"Not this one.\"", "Turning down three tables in a row.", False), ("Easy for the host", "\"Happy to wait.\"", "A few minutes, for the window.", True)),
    note("Why it matters", "Every table you turn down ripples.", "It throws off the host's plan for the next hour."),
    note("To be fair", "Sometimes the room is just full.", "Take the table, enjoy dinner, and ask again next time."),
    tip("Ask early. Be specific. Offer to wait.", "Three small habits. Better seats."),
    end("Seated.", None),
])
C[27] = ("""Want a better table without being that guest?

Put a specific request in the reservation notes, like "a booth if you have one." Mention a birthday or anniversary. And if you want the window, say you're happy to wait a few minutes instead of turning down three tables.

Sometimes the room is just full. Take the table and ask again next time.""",
None,
"#restaurants #diningout #reservations #restaurantlife #hospitality #foodie #datenight")

# ---------------------------------------------------------------- 28
P[28] = ("28_byo_wine", [
    cover("Bringing your own wine to dinner.", "How to not make it weird.", None, None),
    note("First", "Call ahead.", "Not every restaurant allows it, and some aren't legally allowed to. Ask about the policy and the corkage fee."),
    note("Corkage", "A fee to open and pour your bottle.", "It covers the glasses, the service, and the wine sale they're not making."),
    vs("What to bring", ("Awkward", "On their list", "Looks like you're dodging them.", False), ("Nice", "Something special", "An old bottle. A gift.", True)),
    rows("Nice touches", "Things staff remember", [("Offer the server a taste", None), ("Tip a bit extra for the wine service", None), ("Buy one bottle from them too", "Some places waive corkage if you do.")]),
    tip("Call. Bring something special. Buy one too.", "That's all of BYO."),
    end("Cheers.", None),
])
C[28] = ("""Bringing your own wine is fine if you do it right.

Call ahead and ask about the policy and the corkage fee. Bring something special, not a bottle that's already on their list. Offer the server a taste, tip a little extra for the wine service, and think about buying one bottle from them too. Some places waive corkage if you do.""",
None,
"#wine #winelover #byob #corkage #restaurants #diningout #etiquette")

# ---------------------------------------------------------------- 29
P[29] = ("29_host_stand", [
    cover("The host decides where you sit.", "And a few other things.", None, None),
    rows("What the host controls", "More than you'd think", [("Where you sit", None), ("How long you wait", None), ("Which server you get", None)]),
    note("Their job", "Everything at once.", "Reservations, walk-ins, server sections, a table that won't leave. All while smiling at the door."),
    rows("What regulars do", "Small things, every time", [("Say hi", None), ("Give an honest party size", None), ("Call if you're running late", None), ("Say thanks on the way out", None)]),
    note("Over time", "Hosts remember.", "That can mean a better table, a faster seat, or a heads-up when something opens."),
    note("To be fair", "Kindness isn't a coupon.", "You won't always get the best table. You'll never get a worse one for being nice."),
    end("Say hi on the way in.", None),
])
C[29] = ("""The host decides where you sit, how long you wait, and which server you get.

They're also juggling reservations, walk-ins, sections and tables that won't leave. Regulars make it easy: they say hi, give an honest party size, call when they're late and say thanks on the way out.

It won't always get you the best table. It'll never get you a worse one.""",
None,
"#restaurants #restaurantlife #hospitality #diningout #host #foodie #etiquette")

# ---------------------------------------------------------------- 30
P[30] = ("30_thirty_days", [
    cover("Thirty days of menus, hotels and wine.", "Here's the short version.", None, None),
    note("Menus", "No dollar signs. No sweet spot.", "Dropping the $ nudged spending up a bit. The golden triangle was never real."),
    note("Drinks", "One glass, one bottle.", "A glass is often priced at what the bottle cost them. The second-cheapest wine is fine."),
    note("Hotels", "Ask, compare, rebook.", "Late checkout the night before. Compare totals. Rebook refundable rates when prices drop."),
    note("People", "Be nice at the door.", "Hosts, servers and front desk staff remember who made their night easier."),
    tip("You pick next month.", "Comment one: menus, hotels, wine, or behind the scenes.", label="What's next"),
    end("Thanks for reading.", None),
])
C[30] = ("""Thirty days in. The short version:

Menus: no dollar sign nudges spending up a little. The golden triangle was never real.
Wine: one glass often covers the bottle. The second-cheapest is fine.
Hotels: ask the night before, compare totals, rebook when prices drop.
People: be nice at the door. It gets remembered.

What should next month be about? Menus, hotels, wine, or behind the scenes?""",
None,
"#restaurants #travel #foodie #hoteltips #wine #diningout #hospitality")

MENU_LINE = "If you want the cheat sheet (10 things to look for on any menu), comment MENU and I'll DM it to you."

def caption(day):
    text, src, tags = C[day]
    parts = [text.strip(), MENU_LINE]
    if src:
        parts.append("Source: " + src if not src.startswith(("Source", "Sources")) else src)
    parts.append(tags)
    return "\n\n".join(parts) + "\n"


if __name__ == "__main__":
    import sys
    from render3 import carousel
    OUT = "/home/user/workspace/hidden_menu/carousels"
    days = [int(a) for a in sys.argv[1:]] or sorted(P)
    for d in days:
        folder, slides = P[d]
        carousel(f"{OUT}/{folder}", slides, d)
        open(f"/home/user/workspace/hidden_menu/captions/day{d:02d}.txt", "w").write(caption(d))
    print("rendered", days)
