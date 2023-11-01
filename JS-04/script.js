/*
Your job for today is to finish the starSign function.

Find the astrological sign, given the birth details as a Date object.
Start and end dates for zodiac signs very on different resources, 
so we will use this table to get consistent testable results:

Aquarius ----- 21 January - 19 February
Pisces ----- 20 February - 20 March
Aries ----- 21 March - 20 April
Taurus ----- 21 April - 21 May
Gemini ----- 22 May - 21 June
Cancer ----- 22 June - 22 July
Leo ----- 23 July - 23 August
Virgo ----- 24 August - 23 September
Libra ----- 24 September - 23 October
Scorpio ------ 24 October - 22 November
Sagittarius ----- 23 November - 21 December
Capricorn ------ 22 December - 20 January
*/

function starSign(date){
    const astrologySigns = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"]
    const maxDatePerMonth = [21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22]

    const day = 20
    let month = 11

    //check edge case if month = january, day >= 20. This would mean we need to get astrology sign in spot 11 instead of 0,
    if(month === 0 && day <= 20)
        return astrologySigns[11]

    if(maxDatePerMonth[month] < day){
        return astrologySigns[month+1]
    }else{
        return astrologySigns[month]
    }
}