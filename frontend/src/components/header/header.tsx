// import { Logo } from '@/components/logo'
import { Link } from 'react-router-dom'
// import logo from '../../assets/APHRC.png'
import logo from '../../assets/trace.svg'
import { SocialLinks } from '../social-links'
import { Menu } from '../menu'
// import afrijour_logo from '../../assets/afrijour-logo.png'

function Header({ title }: { title?: string }) {
  return (
    <header className="relative py-6">
      <div className="mx-auto w-full max-w-6xl px-6">
        <div className="relative flex items-center justify-between">
          <h1 className="m-0 text-xl font-bold uppercase leading-none">
            <Link to="/" className="flex items-center gap-2 no-underline">
              {/* <Logo /> */}
              {/* <img src={afrijour_logo} alt="logo" style={{height:'10rem'}}/> */}
              <img src={logo} alt="logo" style={{height:'8rem', marginLeft:'-1rem'}}/>
              <span>{title}</span>
            </Link>
          </h1>
          <nav className="flex flex-col items-center mt-16 gap-6 lg:order-1 lg:items-end">
            <Menu className="flex gap-4" />
           
          </nav>
         
        </div>
        <hr  style={{width:'105%', marginTop:'1rem'}}/>
      
      </div>
    </header>
  )
}

export default Header
