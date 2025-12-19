import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BarraSuperior } from './barraSuperior.component';

describe('TopBar', () => {
  let component: BarraSuperior;
  let fixture: ComponentFixture<BarraSuperior>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BarraSuperior]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BarraSuperior);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
