import "./SingleCard.css";
import coverImage from "../assets/cover.png";

export default function SingleCard({ card, handleChoice, flipped, disabled }) {
  const handleClick = () => {
    if (!disabled) {
      handleChoice(card);
    }
  };

  return (
    <div className="card">
      <div className={flipped ? "flipped" : ""}>
        <img className="front" src={card.src} alt="card front" />
        <img
          className="back"
          src={coverImage}
          onClick={handleClick}
          alt="cover"
        />
      </div>
    </div>
  );
}
