import { NewsletterForm } from "@/components/newsletter-form";
import { cn } from "@/utils/cn";
import type { ReactNode } from "react";
import { useEffect, useRef, useState } from "react";
import ScrollReveal from "scrollreveal";
import { Link, useNavigate } from "react-router-dom";
// import lib from '../../assets/lib3.jpg'
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import lib1 from "../../assets/slider/slider1.png";
import lib2 from "../../assets/slider/slider2.png";
import lib3 from "../../assets/slider/slider3.png";
import lib4 from "../../assets/slider/slider4.png";
import { BsJournals } from "react-icons/bs";
import { TfiWrite } from "react-icons/tfi";
import { RiGitRepositoryLine } from "react-icons/ri";

// const history = useHistory();

type ScrollRevealRefElement =
  | HTMLDivElement
  | HTMLHeadingElement
  | HTMLParagraphElement;

function Hero({
  className,
  content,
  illustration,
  title,
}: {
  className?: string;
  content: string;
  illustration?: ReactNode;
  title: string;
}) {
  useEffect(() => {
    if (scrollRevealRef.current.length > 0) {
      scrollRevealRef.current.map((ref) =>
        ScrollReveal().reveal(ref, {
          duration: 3000,
          distance: "40px",
          easing: "cubic-bezier(0.5, -0.01, 0, 1.005)",
          origin: "top",
          interval: 150,
        })
      );
    }

    return () => ScrollReveal().destroy();
  }, []);

  // function onNewsletterSubmit(values: any) {
  //   return new Promise((resolve) => {
  //     setTimeout(() => {
  //       resolve({ values })
  //     }, 1000)
  //   })
  // }
  const navigate = useNavigate();

  //function to redirect to dashboard
  function redirectToDashboard() {
    console.log("jsjsj");
    navigate("/dashboard-main");

    // window.location.href = '/dashboard';
  }

  const addToScrollRevealRef = (el: ScrollRevealRefElement) => {
    scrollRevealRef.current.push(el);
  };
  // const history = useHistory();

  const scrollRevealRef = useRef<ScrollRevealRefElement[]>([]);
  const [roleIndex, setRoleIndex] = useState(0);
  const roles = ["Student!", "Researcher!", "Professor!"];

  useEffect(() => {
    const interval = setInterval(() => {
      setRoleIndex((prevIndex) => (prevIndex + 1) % roles.length);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <section
      className={cn(
        "text-center lg:w-full lg:py-20 lg:text-left mt--4",
        className
      )}
      style={{ padding: "0rem" }}
    >
      <div className="hero mx-auto w-full max-w-6xl px-6">
        <div>
          {/* Have a slider here */}
          <Slider
            dots={true}
            infinite={true}
            speed={2000}
            slidesToShow={1}
            slidesToScroll={1}
            autoplay={true}
            autoplaySpeed={6000}
            fade={true}
            cssEase="linear"
          >
            <div>
              <img
                src={lib1}
                alt="Library Slide 1"
                style={{ width: "100%", height: "380px" }}
              />
            </div>
            <div>
              <img
                src={lib2}
                alt="Library Slide 2"
                style={{ width: "100%", height: "100%" }}
              />
            </div>
            <div>
              <img
                src={lib3}
                alt="Library Slide 3"
                style={{ width: "100%", height: "100%" }}
              />
            </div>
            <div>
              <img
                src={lib4}
                alt="Library Slide 3"
                style={{ width: "100%", height: "100%" }}
              />
            </div>
          </Slider>

          {/* <img src={lib} alt="lib" style={{width:'100%', height:'100%'}}/> */}
        </div>
        <div
          className="mt-6  flex justify-center"
          style={{
            background: "#F4F6FA",
            height: "3rem",
            alignItems: "center",
          }}
        >
          <div>
            <p
              className="text-lg font-small mt-1.5 text-gray-700 dark:text-white text-center"
              style={{ fontSize: "14px" }}
            >
              Looking for an African Journal to publish your article/paper?
            </p>
          </div>

          <div>
            <Link to="/journals">
              <button
                className="text-black ml-3 mb-0 bg-none focus:ring-0 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-green-600 dark:hover:bg-green-700 "
                style={{
                  border: "1px solid #7EC451",
                  borderRadius: "25px",
                  fontSize: "14px",
                  color: "#7EC451",
                  height: "auto",
                  verticalAlign: "middle",
                }}
              >
                Journals Directory
              </button>
            </Link>
          </div>
        </div>

        <div
          className="mt-8"
          style={{
            background: "white",
            height: "3rem",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <div>
            <p
              className="text-lg mr-2 font-small mt-0 text-gray-700 dark:text-white text-center"
              style={{
                fontSize: "38px",
                fontFamily: "verdana",
                color: "#7B7C7C",
                // position: "relative",
              }}
            >
              AfriJour is for every
            </p>
          </div>
          <div style={{ marginTop: "-1.5rem", marginRight: "20%" }}>
            {roles.map((role, index) => (
              <span
                key={index}
                className="role"
                style={{
                  opacity: roleIndex === index ? 1 : 0,
                  transition: "opacity 1s ease-in-out",
                  position: "absolute",
                  // left: 0,
                }}
              >
                <p
                  className="text-lg font-small mt-0 text-gray-700 dark:text-white text-center"
                  style={{
                    fontSize: "38px",
                    fontFamily: "verdana",
                    color: "#8F9AFA",
                    // position: "relative",
                  }}
                >
                  {"    " + role}
                </p>
              </span>
            ))}
          </div>
        </div>

        <div className="flex w-full mt-10 gap-4">
          <div
            className="w-1/3 justify-center "
            ref={addToScrollRevealRef}
            style={{
              display: "grid",
              justifyItems: "center",
              // border: "3px solid #F4F6FA",
              // borderRadius: "19px",
              // background: "#F4F6FA",
            }}
          >
            <BsJournals size={70} color="#78C14A" />

            <p
              className="prose prose-xl mt-2 m-auto text-gray-400 whitespace-nowrap dark:text-white text-center"
              ref={addToScrollRevealRef}
              style={{ fontFamily: "Arial", fontSize: "22px" }}
            >
              Journals
            </p>

            <p
              className="text-lg  mt-1.5 text-gray-500 dark:text-white text-center"
              style={{ fontSize: "14px" }}
            >
              Find out our exclusive directory of more than a thousand African
              Journals.
            </p>
            <Link to="/journals">
              <button
                className="text-black ml-3 mb-0 bg-none focus:ring-0 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-green-600 dark:hover:bg-green-700 "
                style={{
                  border: "1px solid #7EC451",
                  borderRadius: "25px",
                  fontSize: "14px",
                  color: "#7EC451",
                  height: "auto",
                  verticalAlign: "middle",
                }}
              >
                Find Out More
              </button>
            </Link>
          </div>
          <div
            className="w-1/3 justify-center "
            ref={addToScrollRevealRef}
            style={{ display: "grid", justifyItems: "center" }}
          >
            <RiGitRepositoryLine size={70} color="#78C14A" />

            <p
              className="prose prose-xl mt-2 m-auto text-gray-400 whitespace-nowrap dark:text-white text-center"
              ref={addToScrollRevealRef}
              style={{ fontFamily: "Arial", fontSize: "22px" }}
            >
              Partner Repositories
            </p>

            <p
              className="text-lg  mt-1.5 text-gray-500 dark:text-white text-center"
              style={{ fontSize: "14px" }}
            >
              Our Journals are hosted on various repositories. Follow the link
              to find out more.
            </p>
            <Link to="/repositories">
              <button
                className="text-black ml-3 mb-0 bg-none focus:ring-0 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-green-600 dark:hover:bg-green-700 "
                style={{
                  border: "1px solid #7EC451",
                  borderRadius: "25px",
                  fontSize: "14px",
                  color: "#7EC451",
                  height: "auto",
                  verticalAlign: "middle",
                }}
              >
                Find Out More
              </button>
            </Link>
          </div>
          <div
            className="w-1/3 justify-center "
            ref={addToScrollRevealRef}
            style={{ display: "grid", justifyItems: "center" }}
          >
            <TfiWrite size={70} color="#78C14A" />

            <p
              className="prose prose-xl mt-2 m-auto text-gray-400 whitespace-nowrap dark:text-white text-center"
              ref={addToScrollRevealRef}
              style={{ fontFamily: "Arial", fontSize: "22px" }}
            >
              Partner Indexers
            </p>

            <p
              className="text-lg  mt-1.5 text-gray-500 dark:text-white text-center"
              style={{ fontSize: "14px" }}
            >
              Want to know where our platform's Journals are indexed?
            </p>
            <Link to="/indexers">
              <button
                className="text-black ml-3 mb-0 bg-none focus:ring-0 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-green-600 dark:hover:bg-green-700 "
                style={{
                  border: "1px solid #7EC451",
                  borderRadius: "25px",
                  fontSize: "14px",
                  color: "#7EC451",
                  height: "auto",
                  verticalAlign: "middle",
                }}
              >
                Find Out More
              </button>
            </Link>
          </div>
        </div>

        <div
          className="mt-10 bg-#7EC451 grid justify-center"
          style={{
            height: "12rem",
            background: "#7EC451",
            display: "grid",
            justifyItems: "center",
          }}
        >
          <h1
            className="mb-0 mt-4 text-4xl font-bold md:text-5xl "
            ref={addToScrollRevealRef}
            style={{ fontFamily: "Helvetica", color: "white" }}
          >
            AfriJour
          </h1>
          <h4
            className="mb-0 mt-0 text-4xl font-bold md:text-5xl "
            ref={addToScrollRevealRef}
            style={{ fontFamily: "Helvetica", fontSize: "30px" }}
          >
            {title}
          </h4>
          <div className="m-10" ref={addToScrollRevealRef}>
            <p
              className="text-lg  mt-0 text-black dark:text-white text-center"
              style={{ fontSize: "16px", marginTop: "-2rem" }}
            >
              Welcome to AfriJour, your passport to the myriad narratives and
              viewpoints emanating from the heart of Africa. Our platform is
              dedicated to showcasing the vibrant tapestry of African journals
              through the lens of diverse analytics.
            </p>
          </div>
        </div>

        <div ref={addToScrollRevealRef} style={{ marginTop: "2rem", display:'grid', justifyItems:'center'}}>
          <p
            className="text-lg  mt-1.5 text-gray-700 dark:text-white text-center"
            style={{ fontSize: "34px" }}
          >
            Get Started with AfriJour
          </p>
          <button
            style={{
              backgroundColor: "#78C149",
              border: "none",
              borderRadius: "19px",
              padding: "10px 20px",
              color: "white",
              cursor: "pointer",
              width:'15rem'
            }}
            className="-mt-px mt-5 inline-flex cursor-pointer justify-center whitespace-nowrap rounded-sm border-0 bg-gradient-to-r from-secondary-500 to-secondary-400 px-7 py-4 text-center font-medium leading-4 text-white no-underline shadow-lg"
            onClick={redirectToDashboard}
          >
            Go to Dashboard
          </button>
        </div>

        {/*
        
        */}

        <div className="hero-inner relative lg:flex">
          <div className="hero-copy pb-16 pt-10 lg:min-w-[40rem] lg:pr-20 lg:pt-16">
            {/* <div className="mx-auto w-full max-w-3xl">
              <h1
                className="mb-0 mt-0 text-4xl font-bold md:text-5xl "
                ref={addToScrollRevealRef}
                style={{ fontFamily: "Helvetica", color: "#78C149" }}
              >
                AfriJour:
              </h1>
              <h4
                className="mb-0 mt-0 text-4xl font-bold md:text-5xl "
                ref={addToScrollRevealRef}
                style={{ fontFamily: "Helvetica", fontSize: "30px" }}
              >
                {title}
              </h4>

              <p
                className="prose prose-xl mt-2 m-auto text-gray-500"
                ref={addToScrollRevealRef}
                style={{ fontFamily: "verdana", fontSize: "14px" }}
              >
                {content}
              </p>
            </div> */}

            {/* <div ref={addToScrollRevealRef} style={{ marginTop: "2rem" }}>
              <NewsletterForm
                className="mx-auto mt-8 max-w-md lg:mx-0"
                submitText="Go to Dashboard"
                onClick={redirectToDashboard}
                
              />
              <button
                style={{
                  backgroundColor: "#78C149",
                  border: "none",
                  borderRadius: "5px",
                  padding: "10px 20px",
                  color: "white",
                  cursor: "pointer",
                }}
                className="-mt-px inline-flex cursor-pointer justify-center whitespace-nowrap rounded-sm border-0 bg-gradient-to-r from-secondary-500 to-secondary-400 px-7 py-4 text-center font-medium leading-4 text-white no-underline shadow-lg"
                onClick={redirectToDashboard}
              >
                Go to Dashboard
              </button>
            </div> */}
          </div>

          {!!illustration && (
            <div className="relative -mx-6 py-10 lg:mx-0 lg:p-0">
              {illustration}
            </div>
          )}
        </div>
      </div>
    </section>
  );
}

export default Hero;
