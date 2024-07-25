import React from 'react';
import Slider from 'react-slick';
import styled from 'styled-components';

// Styled Components for the partners carousel
const PartnerCarouselContainer = styled.div`
  width: 80%;
  margin: 0 auto;
`;

const PartnerLogo = styled.img`
  max-width: 100%;
  height: auto;
`;

// Dummy data for partner logos
const partnerLogos: string[] = [
  'logo1.png',
  'logo2.png',
  'logo3.png',
  // Add more logo URLs as needed
];

const PartnersCarousel: React.FC = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  };

  return (
    <PartnerCarouselContainer>
      <Slider {...settings}>
        {partnerLogos.map((logo, index) => (
          <div key={index}>
            <PartnerLogo src={logo} alt={`Partner ${index + 1}`} />
          </div>
        ))}
      </Slider>
    </PartnerCarouselContainer>
  );
};

export default PartnersCarousel;
